# Discord Ticket Bot – Production Proposal (Week 7 Task)

## Overview

I developed a Discord ticket bot to manage internal team requests and bug reporting using python. 

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
- 1 CPU  
- 1–2 GB RAM  
- 10–20 GB storage  
- Linux server (e.g. Ubuntu)
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
- Dev time: 1–3 days  

### Ongoing
- VPS hosting: £5–£12/month  
- Storage/backups: £0–£5/month  
- Maintenance time: a few hours/month  

**Total estimate:** ~£5–£20/month

---

## Target Platforms

- Discord (desktop, web, mobile)  
- Server running the bot (Linux/Windows)

---

## System Diagram
