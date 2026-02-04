# Discord Ticketing System Bot

## Overview
This project is a custom Discord ticketing system bot built in Python using `discord.py`.
It allows users to submit support tickets via an interactive button and form inside a Discord server.
Submitted tickets are sent to a private ticket reviewer -only review channel for moderation and response.

This system was designed for an indie game development team to manage bug reports, support requests,
and internal feedback without exposing sensitive information publicly.

---

## Key Features
- Button-based ticket submission (no slash command clutter)
- Modal form for structured ticket input
- Optional GitHub branch field for technical bug reports
- Tickets are forwarded to a private **#ticket-review** channel
- Role-based access for reviewers
- No per-user channel creation (clean server structure)
- Privacy-friendly workflow using hosted image links

---

## User Workflow
1. A user clicks **Submit Ticket** in the `#tickets` channel
2. The user fills in:
   - Subject
   - GitHub branch 
   - Detailed description
3. The ticket is posted as an embed in the staff-only `#ticket-review` channel
4. Reviewers with the **Ticket Reviewer** role can view and manage submissions

If screenshots or videos are needed, users are instructed to provide links
(e.g. Google Drive, OneDrive, Dropbox) directly in the ticket details.

---

## Technical Design
- **Language:** Python 3
- **Library:** discord.py
- **Architecture:** Event-driven Discord bot
- **UI Elements:** Buttons and modals (Discord UI components)
- **Configuration:** Environment variables via `.env` file
- **Permissions:** Role-based access control for reviewers

---

## Environment Variables
The bot uses environment variables to avoid hardcoding sensitive information.

Example `.env` file:
```env
DISCORD_TOKEN=your_bot_token_here
TICKETS_CHANNEL_ID=your_tickets_channel_id
REVIEW_CHANNEL_ID=your_ticket_review_channel_id
STAFF_ROLE_ID=your_ticket_reviewer_role_id
