# Discord Ticket Bot – Production Proposal (Week 7 Task)

## Overview

I developed a Discord ticket bot to manage internal team requests and bug reporting using Python. 

The bot allows team members to submit structured tickets through a form-based system, ensuring that all requests include the necessary information (user, branch, description, optional image links). Submitted tickets are then sent to a private review channel, accessible only to designated roles, allowing for organised tracking and prioritisation.  

---

## Technical Stack

- Python 3  
- discord.py  
- python-dotenv (.env config)  
- Git / GitHub  

Optional (for production):
- Database 
- Logging system

A database ensures tickets are stored securely even if someone deleted them, it can also help track status easier and filter into analytics better. 

A logging system enables developers to know the status of the bot at all times, with specific error messages to help with problem solving. 

---

## Hardware / Cloud Requirements

Minimum:
- 1 shared vCPU (AMD EPYC / Intel Xeon class)
- 1 GB RAM (minimum, however 2GB recommended for scaling)
- 25–40 GB SSD
- Linux distribution (preffered Ubuntu)
- OR Windows (not recommended due to expenses) 

Hosting options:
- Cloud VPS (Virtual Private Server)
- Studio PC

Studio PC is not reccomended due to the energy costs and inconvenience of always running. The small subscription cost of VPS would most likely be worth it in this scenario. Popular providers include: DigitalOcean, AWS, Linode, Vultr. 

---

## Costs

### Initial setup
- VPS setup: ~£5–£10  
- Domain (optional): ~£10/year  
- Dev time: ~8–20 hours

### Ongoing
- VPS hosting: £5–£12/month  
- Storage/backups: £0–£5/month  
- Maintenance time: a few hours/month  

**Total estimate:** ~£5–£20/month

---

## Deployment & Maintenance

The bot is run as a systemd service so it starts on boot and automatically restarts if it crashes.

**Basic setup:**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git -y
git clone <repo-url>
cd discord-ticket-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
**Monitoring:**

```bash
sudo systemctl status ticketbot
journalctl -u ticketbot -f

```

**Maintenence**

The bot will need to be updated peroidically to prevent security issues.

```bash
git pull
pip install -r requirements.txt
sudo systemctl restart ticketbot
```
Logs will also need to be checked weekly for errors.

### AI Declaration

- Helping structure and refine sections of this written report
- Aiding research
