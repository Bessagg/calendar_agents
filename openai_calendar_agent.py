import os
import json
import time  # Import time module for measuring execution time
from langchain.tools import Tool
from langchain_openai import ChatOpenAI  # Updated import for LangChain v0.1+
from langchain.agents import initialize_agent, AgentType
from langchain.schema import SystemMessage
from dotenv import load_dotenv
from google_calendar_helper import GoogleCalendarHelper  # Import your existing class

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Google Calendar Helper
calendar_helper = GoogleCalendarHelper()

# Function to dynamically call calendar functions
def google_calendar_tool(prompt: str):
    """
    Uses LLM to extract the user intent (create, list, update, delete) and executes the corresponding Google Calendar function.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)

    # System message to instruct the LLM
    system_prompt = SystemMessage(
        content="Extract user intent (create, list, update, delete) and event details."
                "Convert relative time experssion to datetime for google calendar format."
                "Return a JSON object with 'action' and 'parameters'."
    )

    extracted_info = llm.invoke([system_prompt, prompt])

    try:
        event_details = json.loads(extracted_info.content)  # Convert LLM response to dict
        action = event_details.get("action")
        params = event_details.get("parameters", {})

        if action == "create":
            return calendar_helper.create_event(params)
        elif action == "list":
            return calendar_helper.list_events(params.get("max_results", 5))
        elif action == "update":
            return calendar_helper.update_event(params.get("event_id"), params)
        elif action == "delete":
            return calendar_helper.delete_event(params.get("event_id"))
        else:
            return "Unknown action. Please specify create, list, update, or delete."
    
    except Exception as e:
        return f"Error processing request: {e}"

# Define a LangChain tool for interacting with Google Calendar
calendar_tool = Tool(
    name="Google Calendar Manager",
    func=google_calendar_tool,
    description="Manages Google Calendar events. Actions: create, list, update, delete."
)

# Initialize LangChain agent with the cheapest OpenAI model
agent = initialize_agent(
    tools=[calendar_tool],
    llm=ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example User Inputs
user_inputs = [
    "Agende uma reunião com Test-Example amanhã às 10h para uma atualização do projeto.",
    "Mostre-me meus próximos 3 eventos.",
    "Atualize a reunião com Test-Example para amanhã às 11h.",
    "Cancele minha reunião com Test-Example."
]

for user_input in user_inputs:
    print("\n\n")
    print(f"\n📝 User: {user_input}")
    print("-"*50)
    start_time = time.time()  # Start timer
    response = agent.invoke(user_input)  # Updated from `agent.run` to `agent.invoke`
    end_time = time.time()  # End timer
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print("-"*50)
    print(f"🤖 Agent: {response}")
    print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")
