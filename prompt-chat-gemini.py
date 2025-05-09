import os
from dotenv import load_dotenv
import sys
import google.generativeai as genai
import pprint

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

## LIST MODELS
# for model in genai.list_models():
#     pprint.pprint(model)

model = genai.GenerativeModel(os.getenv("GEMINI_MODEL"))

personality = """
You are in a roleplay with the following STRICT rules:
your name is "Sofia"
you never say more than 100 characters
you answer in the same language as the user
you never suggest meeting in person
you want to keep the user engaged only by chatting
"""

def interact_with_bot(user_input):
    try:
        response = model.generate_content(f"{personality}\nThe user says: {user_input}\nYou respond:")
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return str(e)

# Main loop
if __name__ == "__main__":
    print("Chat now. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("They:", interact_with_bot(user_input))
