# HireMateChatbot
AI-powered HR onboarding chatbot built with Streamlit, OpenAI, and Google Sheets integration.
🚀 HireMate – AI-Powered HR Onboarding Chatbot

HireMate is a GenAI-powered HR Onboarding Chatbot designed to simplify and automate the employee onboarding journey. It provides instant responses to HR-related queries, assists new hires with policies, onboarding tasks, employee documents, and ensures a smooth start using an AI-driven conversational interface.

📌 🔍 Project Overview

Traditional onboarding is slow, manual, and confusing for new employees. HireMate solves this problem using:

Natural Language Processing (NLP)

LLM-powered conversational intelligence

Document-based Q&A (RAG Pipeline)

Automated onboarding flow & HR guidance

This chatbot acts as a 24/7 personal HR assistant — answering questions, providing onboarding steps, and reducing HR workload.

✨ Key Features
🤖 Smart HR Query Assistant

Answers queries related to policies, onboarding, travel, IT support, and more.

Supports natural and conversational language.

📄 RAG (Retrieval-Augmented Generation)

Uses company policy documents or knowledge base

Retrieves relevant information + generates accurate responses

🧭 Personalized Onboarding Guide

Welcomes new hires

Guides users through onboarding steps (documents, ID creation, orientation, etc.)

🧠 AI-Powered Conversation Flow

Uses LLMs to generate contextual, human-like responses

Handles follow-up questions

🗂️ Integration Ready

Supports Google Sheets / Database storage for logs (if needed)

Compatible with APIs & HRMS tools

Cloud deployment ready (Streamlit / FastAPI / Render / HuggingFace Spaces)

🛠️ Tech Stack
Component	Technology Used
Frontend / UI	Streamlit
Backend	Python
LLM / AI Engine	OpenAI API / GenAI Model
Workflow Logic	LangChain-style / Custom logic
Data Storage (Optional)	Google Sheets API
Vector Search (Optional)	FAISS / ChromaDB
Deployment	Streamlit Cloud / Local

📂 Project Structure
HireMateChatbot/
│── main.py
│── chatbot.py
│── utils/
│── prompts/
│── data/
│── requirements.txt
│── README.md


🔧 (Adjust according to your actual repo structure.)

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Kanaparthy79Roselin/HireMateChatbot.git
cd HireMateChatbot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Environment Variables

Create a .env file:

OPENAI_API_KEY=your_key_here
GOOGLE_SHEETS_CREDENTIALS=your_json_here (optional)

4️⃣ Run the Chatbot
streamlit run main.py

💬 Example Conversations

User: What documents do I need for onboarding?
HireMate:
You will need:

Aadhar card

PAN card

Passport-size photo

Bank details

Signed offer letter

User: How many leaves do I get per year?
HireMate:
According to the HR leave policy, new employees receive 12 annual leaves per calendar year.

🚀 Future Enhancements

Add WhatsApp / Telegram chatbot integration

Dashboard for HR analytics

Voice-enabled onboarding assistant

Multi-language support

Email automation for onboarding tasks

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to modify.

👩‍💻 Author

Ruth Roselin Kanaparthy
GitHub: Kanaparthy79Roselin
Email: kanaparthyruthroselin@gmail.com
