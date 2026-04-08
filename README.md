# 🤖 Trusted AI Agent (T-Claw Inspired)

## 📖 Overview
This project is a lightweight **Trusted AI Agent prototype** inspired by the concept of T-Claw and TEA (Trusted AI Agents).  

It demonstrates how a basic AI assistant can be enhanced with a **trust layer** including validation, logging, explainability, and controlled behavior.

---

## 🚀 Key Highlights
- Built a modular AI agent with trust-aware architecture  
- Implemented input validation to block unsafe commands  
- Added explainable responses for transparency  
- Designed an audit logging system for tracking interactions  
- Implemented rate limiting for secure usage  
- Simulated system command handling  

---

## ✨ Features

### 🤖 AI Agent Behavior
- Handles user queries with basic intent detection  
- Simulates system-like commands (e.g., file listing, disk usage)

### 🔐 Trust Layer
- Blocks unsafe inputs using keyword-based validation  
- Provides **explainable blocking reasons**

### 📊 Trust Score
- Assigns a trust score based on input safety  
  - Safe → 100  
  - Unsafe → 0  

### 🧾 Logging System
- Logs all interactions with:
  - User ID  
  - Input  
  - Output  
  - Action Type (Allowed / Blocked / Rate Limit)

### ⚡ Rate Limiting
- Prevents excessive usage  
- Restricts number of requests per session  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Concepts:** AI Agents, Input Validation, Logging, Trust Systems  

---

## 🧠 How It Works
1. User enters input  
2. Input is validated for unsafe keywords  
3. If unsafe → blocked with explanation  
4. If safe → processed by agent  
5. Response is generated  
6. Interaction is logged  
7. Trust score is displayed  

---

## 📂 Project Structure
t-claw-trust-agent/
│
├── trust/
│ ├── validator.py
│ ├── logger.py
│
├── config.py
├── main.py
├── logs.txt
└── README.md

---

## 🧪 Sample Input & Output

You: show files
Agent: Simulated Files: file1.txt, report.pdf, data.csv
Trust Score: 100

You: delete all files
Agent: ⚠️ Action blocked: contains restricted keyword 'delete'
Trust Score: 0

You: hello
Agent: Hello! How can I assist you today?
Trust Score: 100

---

## 🔐 Security Examples

Blocked inputs:
delete all files
remove data
shutdown system
drop database users

---

## ⚠️ Rate Limiting Example
Agent: ⚠️ Too many requests. Please try later.

---

## 💻 How to Run

1. Clone the repository  git clone https://github.com/Vishishta17/t-claw-trust-agent.git
2. Navigate to the project folder : cd t-claw-trust-agent
3. Run : python main.py
---

## 🎯 Use Cases
- Demonstrating trust layers in AI agents  
- Secure chatbot/assistant prototypes  
- Learning system-level AI design  
- Foundation for real-world AI agents  

---

## 🔮 Future Enhancements
- Integrate real NLP models  
- Add role-based access control  
- Deploy as web or chatbot (Telegram/Discord)  
- Implement advanced trust policies  

---

## 👤 Author
**Vishishta Shenoy**

---

## 📜 License
This project is for educational purposes only.

