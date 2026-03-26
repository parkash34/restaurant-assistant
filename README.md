# 🍕 Muzo: Pizza Hut Restaurant Assistant API

A REST API that runs an AI-powered customer service assistant for Pizza Hut. Customers can chat with Muzo to ask about the menu, make reservations, or get help with complaints. The API enforces strict structured JSON outputs, maintains session memory, and dynamically injects daily context — powered by LLaMA 3.3 70B via Groq.

---

## ⚡ Tech Stack

| | |
|---|---|
| **Framework** | FastAPI |
| **AI Model** | LLaMA 3.3 70B via Groq API |
| **Language** | Python |
| **Output Format** | Strict JSON Parsing |
| **Memory** | In-memory per session |

---

## 🎭 Assistant Capabilities

| Category | How It Handles It |
|---|---|
| `Menu` | Recommends items, answers questions about spicy options, and pitches today's dynamic specials. |
| `Reservation` | Checks dynamic table availability in real-time and assists with booking dates and times. |
| `Complaint` | Apologizes professionally, recognizes busy days, and attempts to resolve customer dissatisfaction. |
| `Other` | Strict guardrails detect off-topic questions (like geography or coding) and gently redirect the user back to restaurant services. |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone [https://github.com/parkash34/YOUR-REPO-NAME.git](https://github.com/parkash34/YOUR-REPO-NAME.git)
cd YOUR-REPO-NAME