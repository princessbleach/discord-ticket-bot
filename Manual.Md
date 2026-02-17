# Discord Ticket Bot  
**User and developer manual**

## Overview  
The Discord Ticket Bot is a Python-based support and review tool.  
Users submit structured tickets through a panel in **#ticket**, and submissions are automatically sent to **#ticket-review** where authorised staff can assess them.

---

## User Guide  

### Submitting a Ticket  
1. Open the **#ticket** channel.  
2. Press **Submit Ticket** on the panel.  
3. Enter required details:  
   - GitHub branch  
   - Description  
   - Image links (optional)  
4. Submit the form.  

The ticket is forwarded to **#ticket-review** for staff evaluation.

---

## Staff Guide  

### Reviewing  
- Monitor **#ticket-review** for new tickets.  
- Check branch, description clarity, and any provided images.  
- Provide feedback, approval, or request changes based on team workflow.  

---

## Developer Guide  

### Structure  
    discord-ticket-bot/  
    ├── bot.py — ticket panel, form handling, routing to #ticket-review  
    ├── requirements.txt — dependencies  
    └── .env — secure bot token (not public)  

### Running  

**Install dependencies**  
    pip install -r requirements.txt  

**Start the bot**  
    python bot.py  

---

## Security  
- Keep the bot token private.  
- Limit review access to authorised roles (e.g., Ticket Reviewer).  
- Keep dependencies updated.  

---

## Future Improvements  
- Database storage  
- Status tracking  
- GitHub integration  
- Web dashboard  
