import os
import openai
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Step 1: Set environment variables (make sure these are correct)
os.environ["OPENAI_API_KEY"] = "sk..."
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_creds.json"

# Step 2: Spreadsheet ID (From the Google Sheets URL)
SPREADSHEET_ID = "Your-spreadsheet-ID"

# ✅ Properly authorize Google Sheets with scope
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("google_creds.json", scopes=scope)
gc = gspread.authorize(creds)
worksheet = gc.open_by_key(SPREADSHEET_ID).sheet1

# Step 4: Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 5: Simple FAQ-based tool
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

# Step 6: Log conversation to Google Sheet
def log_to_google_sheet(name, task, status="In Progress"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.append_row([name, task, status, timestamp])

# Step 7: Chatbot main function
def hiremate_chatbot():
    name = input("Enter your name: ")
    print("\n👋 Welcome to HireMate – your HR Onboarding Assistant!")
    print("Type your question or type 'exit' to end the conversation.\n")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("HireMate: Goodbye! All the best! 🎉")
            break
        response = onboarding_faq_tool(query)
        print("HireMate:", response)
        log_to_google_sheet(name, query, "Logged")

# Step 8: Start the chatbot
if __name__ == "__main__":
    hiremate_chatbot()
