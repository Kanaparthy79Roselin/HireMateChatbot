import streamlit as st
import openai
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


# API Key & Google Auth
openai.api_key = "sk..."  # Use your real key
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("google_creds.json", scopes=scope)
# Authorize gspread
gc = gspread.authorize(creds)
client = gspread.authorize(creds)

# Step 2: Spreadsheet ID (From the Google Sheets URL)
SPREADSHEET_ID = "Your-spreadsheet-ID"
sheet = gc.open_by_key(SPREADSHEET_ID).sheet1


def onboarding_faq_tool(query):
    faqs = {
        "documents": "Please upload your ID proof, address proof, and educational certificates.",
        "orientation": "Your orientation is scheduled on the first Monday after your joining date.",
        "benefits": "You are eligible for health insurance, paid leaves, and performance bonuses."
    }
    for key in faqs:
        if key in query.lower():
            return faqs[key]
    return "I'll forward this to HR for clarification."

def log_to_google_sheet(name, task, status="Logged"):
    sheet.append_row([name, task, status])

# Streamlit UI
st.title("📋 HireMate HR Onboarding Chatbot")
name = st.text_input("Enter your name:")

if name:
    user_input = st.text_input("Ask a question:")
    if user_input:
        response = onboarding_faq_tool(user_input)
        log_to_google_sheet(name, user_input, "Logged")
        st.success(f"HireMate: {response}")
