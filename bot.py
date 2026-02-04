import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

# ------------------ ENV ------------------
TOKEN = os.getenv("DISCORD_TOKEN")
TICKETS_CHANNEL_ID = int(os.getenv("TICKETS_CHANNEL_ID"))      # #tickets
REVIEW_CHANNEL_ID = int(os.getenv("REVIEW_CHANNEL_ID"))        # #ticket-review
TICKET_REVIEWER_ROLE_ID = int(os.getenv("STAFF_ROLE_ID"))      # Ticket Reviewer role ID

# ------------------ BOT SETUP ------------------
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# ------------------ HELPERS ------------------
def new_ticket_id() -> str:
    return f"T{int(time.time())}"


def clean_optional(value: Optional[str]) -> str:
    v = (value or "").strip()
    return v if v else "Not provided"


# ------------------ MODAL ------------------
class TicketModal(discord.ui.Modal, title="Submit a Ticket"):
    subject = discord.ui.TextInput(
        label="Subject",
        placeholder="Short summary of the issue",
        max_length=80
    )

    # ✅ REQUIRED now (required=True by default, but we set it explicitly)
    branch = discord.ui.TextInput(
        label="GitHub branch (required)",
        placeholder="e.g. main, develop, feature/combat-fix",
        max_length=80,
        required=True
    )

    image_links = discord.ui.TextInput(
        label="Image / video links (optional)",
        placeholder="Paste links (Google Drive, OneDrive, Dropbox, Imgur, etc.)",
        style=discord.TextStyle.paragraph,
        max_length=500,
        required=False
    )

    details = discord.ui.TextInput(
        label="Details",
        placeholder="Steps to reproduce, device, expected vs actual behaviour",
        style=discord.TextStyle.paragraph,
        max_length=1500
    )

    def __init__(self, user: discord.Member):
        super().__init__()
        self.user = user
        self.ticket_id = new_ticket_id()

    async def on_submit(self, interaction: discord.Interaction):
        if interaction.guild is None:
            return await interaction.response.send_message(
                "This only works inside a server.",
                ephemeral=True
            )

        if interaction.channel_id != TICKETS_CHANNEL_ID:
            return await interaction.response.send_message(
                f"Please submit tickets in <#{TICKETS_CHANNEL_ID}> only.",
                ephemeral=True
            )

        review_channel = interaction.guild.get_channel(REVIEW_CHANNEL_ID)
        if not isinstance(review_channel, discord.TextChannel):
            return await interaction.response.send_message(
                "Ticket review channel not found. Please contact staff.",
                ephemeral=True
            )

        reviewer_role = interaction.guild.get_role(TICKET_REVIEWER_ROLE_ID)

        embed = discord.Embed(
            title=f"🎫 New Ticket {self.ticket_id}: {self.subject.value}",
            description=self.details.value,
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="From",
            value=f"{self.user.mention} (`{self.user.id}`)",
            inline=False
        )

        # branch is required, but we still strip it to keep it clean
        embed.add_field(
            name="Branch",
            value=self.branch.value.strip(),
            inline=True
        )

        if self.image_links.value and self.image_links.value.strip():
            embed.add_field(
                name="Image / Video Links",
                value=self.image_links.value[:1024],
                inline=False
            )

        try:
            await review_channel.send(
                content=reviewer_role.mention if reviewer_role else None,
                embed=embed
            )
        except discord.Forbidden:
            return await interaction.response.send_message(
                "I don’t have permission to post in the review channel.",
                ephemeral=True
            )

        await interaction.response.send_message(
            f"✅ Ticket submitted successfully (**{self.ticket_id}**). Thank you!",
            ephemeral=True
        )


# ------------------ PANEL VIEW ------------------
class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="🎫 Submit Ticket",
        style=discord.ButtonStyle.green,
        custom_id="submit_ticket"
    )
    async def submit_ticket(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        if interaction.channel_id != TICKETS_CHANNEL_ID:
            return await interaction.response.send_message(
                f"Please use <#{TICKETS_CHANNEL_ID}> to submit tickets.",
                ephemeral=True
            )

        await interaction.response.send_modal(TicketModal(interaction.user))


# ------------------ EVENTS ------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ✅")
    bot.add_view(TicketView())


# ------------------ COMMAND ------------------
@bot.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def ticketpanel(ctx: commands.Context):
    if ctx.channel.id != TICKETS_CHANNEL_ID:
        return await ctx.send(
            f"Use this command in <#{TICKETS_CHANNEL_ID}> only."
        )

    embed = discord.Embed(
        title="Support Tickets",
        description=(
            "Press **Submit Ticket** to send an issue to the team.\n\n"
            "**GitHub branch is required** for technical tracking.\n"
            "If you have screenshots or videos, paste **links** "
            "(Google Drive, OneDrive, Dropbox, Imgur, etc.) in the form."
        ),
        color=discord.Color.blurple()
    )

    await ctx.send(embed=embed, view=TicketView())


# ------------------ RUN ------------------
bot.run(TOKEN)
