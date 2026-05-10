# 🏠 Pinyo Empire — Command Center
*Your second brain. Everything is here.*

---

## ⚡ Empire Pulse

```dataview
TABLE status, notes AS "Notes"
FROM "empire-status"
```

---

## 🔥 Active Sprint

```dataview
TABLE status AS "Status"
FROM "00-load-me"
WHERE file.name = "SPRINT"
```

> Open [[SPRINT|Full Sprint View]] for all active items.

---

## 🏢 Businesses

| Business | Status | Note |
|----------|--------|------|
| [[aura-thai\|🍜 Aura Thai]] | 🟡 Active | Lavu integration blocked |
| [[vine-arbitrage\|🌿 Vine Arbitrage]] | 🟢 Running | Artie managing |
| [[pinyo-farms\|🌾 Pinyo Farms]] | ⏳ Planning | Market validation needed |
| [[ai-ventures\|🤖 AI Ventures]] | ⏳ Planning | Restaurant subscription stream |
| [[roam\|🌍 Roam]] | ⏳ Planning | Content plan needed |

---

## 🧠 The Brain

| File | What It Is |
|------|-----------|
| [[EMPIRE_STATUS]] | Live status of all systems |
| [[SPRINT]] | Active items this sprint |
| [[MASTER_OPEN_ITEMS]] | Full open items history |
| [[SESSION_HISTORY]] | Every session logged |
| [[CLAUDE-CORE]] | Claude's identity + protocols |
| [[SHARED-CORE]] | Empire rules + mental models |

---

## 📥 Inbox

```dataview
LIST
FROM "_inbox"
SORT file.ctime DESC
```

---

## 🤝 The Board

| Role | Agent | Handles |
|------|-------|---------|
| **Chairman** | Chris | Decisions, approvals, physical actions |
| **Strategist** | Claude | Plans, builds, architects, writes |
| **Executor** | Artie | Runs, reports, executes SOPs |

---

*Last updated by Claude. Auto-syncs via Obsidian Git.*
