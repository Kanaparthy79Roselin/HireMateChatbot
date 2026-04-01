import streamlit as st
import openai
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

openai.api_key = st.secrets["OPENAI_API_KEY"]

scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=scope
)
gc = gspread.authorize(creds)
SPREADSHEET_ID = "17IpIlYiCjYW0geK0dwKAl87vAUMU34Y5wvthZsqrLII"
sheet = gc.open_by_key(SPREADSHEET_ID).sheet1

SYSTEM_PROMPT = """You are HireMate, a friendly HR onboarding assistant.
Answer new employee questions about documents, orientation, benefits,
and company policies. Be warm, helpful, and concise."""

def log_to_google_sheet(name, question, answer):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([name, question, answer, timestamp])

st.title("📋 HireMate HR Onboarding Chatbot")
name = st.text_input("Enter your name:")

if name:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_input := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}]
                     + st.session_state.messages
        )
        reply = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)

        log_to_google_sheet(name, user_input, reply)}")
