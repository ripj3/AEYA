# README.md — Tunes Do Travel Automation Stack

## 🎶 Overview
Tunes Do Travel is a modular, low-cost, automation-first creative system for exploring global music culture. Built for performance on the free-tier of **n8n**, it connects:
- Aeya (AI researcher + narrator)
- Frank (financial advisor agent)
- Google Sheets (as database)
- Stripe + Zapier (as income/event input)
- Wavespeed.ai (video platform)
- Kokora (narrative voice synthesis)

---

## 🧩 Components

### 🧠 `content_orchestration_core.json`
- Central workflow
- Triggers: chat
- Stages: research → script → QC → approval → Kokora → video (Pika or Lumia via Wavespeed.AI)
- Writes to: `Episodes`, `Video_Log`, `Notification_Log`

### 🤖 `ensemble-review-subflow.json`
- LLM-based quality check
- Uses Hugging Face API
- Writes flagged issues + votes to `LLM_Review_Log`

### 💸 `trigger-financial-upgrades-and-debt-paydown.json`
- Chat with Frank → loads logs → evaluates:
  - VISA debt paydown (-1500)
  - Tech fund contribution (up to 4k)
  - QuickBooks, Lindy, Devin triggers 
- Writes to: `System_Financial_Plan`

### 📊 Google Sheets
Includes 6 synchronized tabs:
- `Episodes`
- `Video_Log`
- `LLM_Review_Log`
- `Notification_Log`
- `Payments_Log`
- `Expenses_Log`
- `System_Financial_Plan`

---

## ⚙️ Setup
- Follow `SETUP.md`
- Import .json workflows into n8n
- Use `.env` file to configure keys
- All executions are under free-tier budget (< 5 workflows, 1000 runs/mo)

---

## 💬 Agents

### Aeya
- Creative orchestrator
- Writes scripts, runs QC, routes videos
- Sends approvals to tunesdotravel@gmail.com

### Frank
- Embedded in financial JSON
- Monitors income, expenses, upgrades
- Encouraging tone, but grounded in limits



## 🚀 Goals
- Discover and celebrate under-represented music cultures
- Automate everything possible
- Stay lean until scaling is justified

---

## 🛠️ Status
- ✅ Sheets aligned
- ✅ JSON workflows
- ✅ Frank & Aeya chat interface working
- ⏳ Awaiting API keys / deployment

---

## 📩 Questions?
Email: liz@lizmclellan.com  
Site: https://lizmclellan.com

Made with rhythm and recursion.
