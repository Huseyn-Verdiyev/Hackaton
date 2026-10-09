# 🚀 RetentionAI - Intelligent Customer Feedback & Product Evolution Agent

**RetentionAI** is an Enterprise AI Agent designed to solve one of the most critical challenges for businesses: **Customer Churn and Stagnant Product Development.**

In today's competitive market, companies lose millions when they ignore customer feedback. RetentionAI bridges the gap between what customers complain about and what the company does next.

## 🔥 Why is this a 100% Market Need? (The Winning Factor)
1. **Instant Customer Retention:** When a customer leaves a negative review or churns, the AI Agent instantly analyzes the sentiment and context, generating a **hyper-personalized special offer** or apology to win them back immediately.
2. **Automated Product Evolution:** It aggregates thousands of feedback tickets, identifies core issues, and writes actionable **Feature Requests or Bug Reports** for the product and engineering teams.
3. **Zero Human Bottleneck:** It acts as a 24/7 Customer Success Manager and Product Manager working simultaneously.

---

## 🏗️ Architecture & How It Works

1. **Ingestion:** Receives customer feedback (via API, CSV, Intercom, Zendesk, App Store reviews).
2. **Sentiment & Intent Analysis:** Uses LLM (Large Language Models) to understand the emotion and the core problem (e.g., "Pricing is too high", "The mobile app crashes on login").
3. **Agentic Actions (Dual Pathway):**
   - **Pathway A (Customer-Facing):** Generates a custom compensation offer (e.g., "We are sorry the app crashed. Here is a 30% discount code for your next month while our team fixes this.")
   - **Pathway B (Company-Facing):** Alerts the development team: "Priority: High. Multiple users reporting mobile app crash on login. Suggested action: Inspect Auth module."

---

## 💻 Tech Stack
- **AI/LLM Core:** OpenAI GPT-4 / Anthropic Claude (via LangChain or LiteLLM)
- **Backend:** Python
- **Data format:** JSON (Easily adaptable to databases like PostgreSQL or Vector DBs for RAG)

---

## 📂 Project Structure

```text
├── data/
│   └── feedback.json       # Mock dataset containing customer reviews
├── src/
│   ├── agent.py            # The main Orchestrator Agent
│   ├── analyzer.py         # LLM logic to analyze sentiment and extract product issues
│   └── offer_generator.py  # Logic to create personalized customer offers
├── README.md
└── requirements.txt
```

## 🚀 How to Run the Prototype

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API Key (or other LLM provider):
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```
3. Run the Agent:
   ```bash
   python src/agent.py
   ```

*Built for Starnest Hackathon by a future winner! 🏆*
