import streamlit as st
import openai

# 🔐 Load API key safely
openai.api_key = st.secrets.get("OPENAI_API_KEY")

SYSTEM_PROMPT = """You are HireMate, a friendly HR onboarding assistant.
Answer new employee questions about documents, orientation, benefits,
and company policies. Be warm, helpful, and concise."""

st.title("📋 HireMate HR Onboarding Chatbot")

name = st.text_input("Enter your name:")

# ✅ Simple fallback (VERY IMPORTANT)
def fallback_response(query):
    faqs = {
        "documents": "Please upload your ID proof, address proof, and educational certificates.",
        "orientation": "Your orientation is scheduled on the first Monday after your joining date.",
        "benefits": "You are eligible for health insurance, paid leaves, and performance bonuses."
    }
    for key in faqs:
        if key in query.lower():
            return faqs[key]
    return "I'll forward this to HR for clarification 💌"

if name:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_input := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.write(user_input)

        try:
            # 🔥 Try OpenAI first
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # safer model
                messages=[{"role": "system", "content": SYSTEM_PROMPT}]
                         + st.session_state.messages
            )
            reply = response.choices[0].message.content

        except Exception as e:
            # 💡 If OpenAI fails → fallback
            reply = fallback_response(user_input)

        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.write(reply)