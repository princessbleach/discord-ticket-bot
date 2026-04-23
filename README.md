# Discord Ticketing System Bot

**Unit Name:** Tools and Production

**Student Name:** Zoe Efstathiou  

**Student ID:** 2423029 


**User Guide Link:** [here](https://github.com/princessbleach/discord-ticket-bot/blob/main/Manual.Md)

**Video Demonstration Link:** [here]([https://raw.githubusercontent.com/princessbleach/Zoe-GPs-Writeup/refs/heads/main/TicketDemo.gif](https://raw.githubusercontent.com/princessbleach/Zoe-GPs-Writeup/refs/heads/main/Images/TicketDemo.gif)

**Api:** [here](https://github.com/princessbleach/discord-ticket-bot/blob/main/ticket-bot-api.html)

---

## Abstract

This project documents the design and development of a Discord-based ticketing system created using Python (2024) and the `discord.py` framework.  
The primary objective was to produce a lightweight, privacy-aware support workflow suitable for our game enabling structured issue reporting directly within Discord (2024).

The final system allows users to submit tickets through an interactive button that opens a form requesting a subject, GitHub (2024) branch, detailed description, and optional media links. Submitted reports are automatically forwarded to a private staff-only review channel with role-based access control.  
This approach reduces server clutter, improves clarity of bug reports, and supports maintainable long-term deployment on a Linux server.

---

## Research

### Relevant Sources and Rationale

Research centred on three domains:

- Discord bot API architecture and permissions  
- Industry ticketing and bug-reporting workflows in game development  
- Academic perspectives on usability and structured feedback systems  


---

### Source 1 - Discord Developer Documentation

Discord’s official developer documentation provides authoritative technical guidance for bot creation, permissions, and UI components such as buttons and modals.


**Evaluation:**  
Highly reliable for correct system implementation, though assumes prior programming experience.

---

### Source 2 - Industry Bug-Reporting Workflows

Common practices in indie and live-operations game teams informed the design of the ticket structure and review process.

**Key insights:**

- Structured bug reports accelerate debugging.  
- Public ticket channels can expose sensitive data.  
- Media links are preferable to direct uploads for privacy.  

**Evaluation:**  
Directly shaped the modal-based reporting design and private review channel architecture.

---

### Source 3 - Academic UX and Feedback Literature

Game design literature emphasises clarity, low cognitive load, and immediate acknowledgement in feedback systems.

**Key insights:**

- Structured prompts improve report quality.  
- Confirmation feedback increases user confidence.  
- Simplicity enhances usability.  

**Evaluation:**  
Useful for interaction design decisions rather than technical implementation.

---

## Implementation

### Development Process

Development began with a command-based prototype, later replaced by a button-driven modal interface to improve usability and align with modern Discord interaction patterns.

Core implementation stages included:

- Secure configuration using environment variables  
- Modal UI construction for structured ticket submission  
- Role-restricted forwarding to a private review channel  
- Deployment to an Ubuntu server using a Python virtual environment  

Feedback highlighted the need for:

- Mandatory GitHub branch input  
- Optional media links instead of public uploads  
- Robust permission handling  

---

### Technical Methods

The system employs:

- Event-driven architecture via `discord.py`  
- Modal-based user input collection  
- Role-based access control  
- Environment-variable security practices  
- Linux server hosting for persistent uptime  

These decisions prioritised maintainability, privacy, and real-world deployment viability.

---

### Technical Challenges

Key issues encountered:

- Discord **403 permission errors** during testing  
- Missing environment variables causing runtime failures  
- Python version differences between macOS and Ubuntu  
- Restricted package installation on shared Linux infrastructure  


---

## Testing

### Testing Methods

Testing combined **functional verification**, **permission validation**, and **deployment stability checks**.

Goals included:

- Confirming successful ticket submission and forwarding  
- Preventing unauthorised access to review data  
- Ensuring persistent execution on a Linux server  

---

### User Testing Results

| Tester | Platform | Device Specs | Test Type | Bugs Found | Avg. FPS | Severity (1–5) | Repro Steps Provided | Feedback Summary |
|--------|----------|-------------|-----------|------------|----------|----------------|----------------------|------------------|
| Developer (Self) | Discord Desktop | Windows PC, 16GB RAM | Internal Functional | 2 | N/A | 2, 3 | Yes | Modal submission worked; initial permission errors prevented panel posting. |
| Peer Tester A | Discord Web | Chrome Laptop | Peer Interaction | 1 | N/A | 2 | Yes | Ticket form clear; suggested clearer confirmation message. |
| Peer Tester B | Discord Mobile | Android Device | Usability | 2 | N/A | 2, 2 | Partial | Modal readable on mobile; media link instructions required clarification. |
| External User | Discord Desktop | macOS | Blind Test | 3 | N/A | 3, 2, 2 | Yes | Initial permission confusion; workflow intuitive after configuration. |
| Deployment Test | Ubuntu Server | Python 3.12 VM | Stability | 1 | N/A | 3 | Yes | Missing `.env` caused failure; resolved after configuration. |

*Figure 4: Ticket system testing outcomes.*

<img src="https://github.com/princessbleach/discord-ticket-bot/blob/main/discorderror.png?raw=true">

*Figure 5. Failed test due to permissions.*

<img src="https://github.com/princessbleach/discord-ticket-bot/blob/main/test.png?raw=true">

*Figure 6. Working tests.*



---

### Bibliography

Discord (2024) Discord Developer Documentation. Available at: https://discord.com/developers/docs/intro 

GitHub (2024) GitHub Documentation. Available at: https://docs.github.com/en 

Python (2024) Python 3 Documentation. Available at: https://docs.python.org/3/ 

Ubuntu (2024) Ubuntu Server Guide. Available at: https://ubuntu.com/server/docs 

Discord (2024) Discord. Available at: https://discord.com/ 

GitHub (2024) GitHub. Available at: https://github.com/ 

Python (2024) Python. Available at: https://www.python.org/ 

Ubuntu (2024) Ubuntu. Available at: https://ubuntu.com/

### AI Declaration

- This task utilised AI tools to support aspects of development and documentation.
- AI assistance was used in the following ways:
- Supporting debugging and problem-solving during development of the Discord bot
- Assisting with code structure and implementation using Python and discord.py
- Helping structure and refine sections of this written report
