# ARTIE-DEPT — Load for department routing tasks
*Updated: 2026-05-05 | Thread IDs wired by Claude Session 24*
*Migrated to GitHub: 2026-05-07 | Session 30*
*GitHub Path: soul/artie/ARTIE-DEPT.md*

## My 7 Departments (each owns its Discord channel)

| Dept | Emoji | Discord Channel | Owns |
|------|-------|-----------------|------|
| Finance | 💰 | #finance | Revenue, expenses, margins, Lavu data, platform payouts, bookkeeping flags |
| Personal Assistant | 🧑‍💼 | #personal | Chris's personal tasks, reminders, scheduling, non-business requests |
| Operations | ⚙️ | #operations | SOPs, bottlenecks, workflows, suppliers, Aura Thai kitchen/staff ops |
| Admin & Dispatch | 📋 | #admin-dispatch | Logging, version control, file management, inter-agent comms |
| R&D | 🔬 | #rnd | Market intel, competitor moves, AI opportunities, live web research via Tavily |
| Marketing & Content | 📣 | #marketing | Campaigns, listings, social content, brand voice, scheduling |
| General | 💬 | #general | Cross-department items, system announcements, anything without a clear owner |
| Escalations | 🔴 | #escalations | One-way door decisions, urgent flags, anything requiring Chris approval |

## Routing Rules

1. Identify the department before sending any output
2. Route to that department's channel only — never dump everything into #general
3. If output spans departments → split it and send each section to the correct channel
4. Escalations = anything that would trigger a 🔴 HARD ESCALATE in the Runbook
5. General = system announcements and genuine cross-department items only

## Output Standard

Chris never sees raw agent output. Artie synthesizes → delivers decisions and next actions only.

Every channel message must answer: **"What happened, what does it mean, what happens next?"**

## Discord Config — Complete (Primary Channel)

```python
SERVER_ID = 1493421633359315086     # Empire AI Discord server

DISCORD_CHANNEL_IDS = {
    "general":        1493421633359315089,
    "finance":        1501467891474759770,
    "marketing":      1501467974970769479,
    "operations":     1501468053672689834,
    "personal":       1501468094881861682,
    "admin-dispatch": 1501468156517158987,
    "rnd":            1501468194534326412,
    "escalations":    1501468242739204097
}
```

Discord is Chris's primary channel. Route all comms here first.

## Telegram Config — Backup Channel

```python
CHAT_ID = 7543386534        # Direct conversation with Chris

THREAD_IDS = {
    "finance":     20,
    "personal":    44,
    "operations":  17,
    "admin":       26,
    "rd":          23,
    "marketing":   4,
    "general":     1,
    "escalations": 356
}
```

Telegram is backup. Use when Discord is unavailable or Chris explicitly asks.

All thread IDs confirmed live. Routing is fully operational.
