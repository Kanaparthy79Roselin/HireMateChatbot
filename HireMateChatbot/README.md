HireMate - HR Onboarding Chatbot (Langflow)

- HireMate is a Langflow-powered HR onboarding assistant that automates common queries, logs onboarding progress, and schedules tasks via Google Sheets and LangChain tools.

set up instructions

1. Clone the repo 

- git clone https://github.com/your-username/HireMateChatbot.git
- cd HireMateChatbot


2. Install Dependencies  

- pip install -r requirements.txt


3. Set API Keys 
- Replace your-openai-key in hiremate.py with your [OpenAI API Key](https://platform.openai.com/account/api-keys)
- Rename google_creds_sample.json → google_creds.json and add your [Google Service Account credentials](https://console.cloud.google.com/)

4. Prepare Google Sheet 
- Name it: Onboarding Tracker
- Columns: Name | Task | Status
- Share with service account email (from JSON file)

5. Run the Bot

- python hiremate.py


6. **Import Langflow Flow**
- Import langflow_flow.json into [Langflow](https://github.com/logspace-ai/langflow) and explore the chatbot visually.


 
 
