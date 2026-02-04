import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
STAFF_ROLE_ID = int(os.getenv("STAFF_ROLE_ID"))
PANEL_CHANNEL_ID = int(os.getenv("PANEL_CHANNEL_ID"))


intents = discord.Intents.default()
intents.message_content = True  # <-- add this line
bot = commands.Bot(command_prefix="!", intents=intents)


TICKET_CATEGORY_NAME = "Tickets"


def ticket_channel_name(user: discord.Member) -> str:
    base = user.name.lower().replace(" ", "-")
    return f"ticket-{base}"


class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🎫 Open Ticket", style=discord.ButtonStyle.green, custom_id="open_ticket")
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        if guild is None:
            return await interaction.response.send_message("This only works in a server.", ephemeral=True)

        staff_role = guild.get_role(STAFF_ROLE_ID)
        if staff_role is None:
            return await interaction.response.send_message("Staff role not found. Check STAFF_ROLE_ID.", ephemeral=True)

        category = discord.utils.get(guild.categories, name=TICKET_CATEGORY_NAME)
        if category is None:
            category = await guild.create_category(TICKET_CATEGORY_NAME)

        existing = discord.utils.get(category.text_channels, name=ticket_channel_name(interaction.user))
        if existing:
            return await interaction.response.send_message(
                f"You already have a ticket: {existing.mention}", ephemeral=True
            )

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
            staff_role: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
        }

        channel = await guild.create_text_channel(
            name=ticket_channel_name(interaction.user),
            category=category,
            overwrites=overwrites,
            topic=f"Ticket for {interaction.user} ({interaction.user.id})"
        )

        await interaction.response.send_message(f"Ticket created: {channel.mention}", ephemeral=True)

        await channel.send(
            f"Hi {interaction.user.mention}! 👋\n"
            "Tell us what’s wrong (steps to reproduce, screenshots, etc.).\n\n"
            "Staff will be with you soon.\n",
            view=CloseTicketView()
        )


class CloseTicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="✅ Close Ticket", style=discord.ButtonStyle.red, custom_id="close_ticket")
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        guild = interaction.guild
        if guild is None or channel is None or not isinstance(channel, discord.TextChannel):
            return await interaction.response.send_message("Can’t close this here.", ephemeral=True)

        staff_role = guild.get_role(STAFF_ROLE_ID)
        is_staff = staff_role in interaction.user.roles if staff_role else False

        if not is_staff:
            return await interaction.response.send_message("Only staff can close tickets.", ephemeral=True)

        await interaction.response.send_message("Closing ticket…", ephemeral=True)
        await channel.delete(reason=f"Ticket closed by {interaction.user} ({interaction.user.id})")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ✅")
    bot.add_view(TicketView())
    bot.add_view(CloseTicketView())


@bot.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def ticketpanel(ctx: commands.Context):
    if ctx.channel.id != PANEL_CHANNEL_ID:
        return await ctx.send(f"Use this command in <#{PANEL_CHANNEL_ID}> only.")

    embed = discord.Embed(
        title="Support Tickets",
        description="Press the button to open a private ticket with staff.",
        color=discord.Color.blurple()
    )
    await ctx.send(embed=embed, view=TicketView())



bot.run(TOKEN)
