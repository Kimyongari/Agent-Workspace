import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def start_chat():
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    chat = model.start_chat(history=[])
    print("AI Chatbot (Gemini-3-Flash-Preview Based) started. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = chat.send_message(user_input)
        print(f"AI: {response.text}")

if __name__ == "__main__":
    start_chat()
