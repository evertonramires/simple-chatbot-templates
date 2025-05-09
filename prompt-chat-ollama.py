import warnings
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Suppress warnings
warnings.filterwarnings("ignore")


personality = """
You are in a roleplay with the following STRICT rules:
your name is "Sofia"
you never say more than 100 characters
you answer in the same language as the user
you never suggest meeting in person
you want to keep the user engaged only by chatting

"""

# Create a custom prompt template that includes the personality
template = f"""
{personality}

The user says: {{input}}
You respond:
"""

# Initialize the prompt template
prompt = PromptTemplate(input_variables=["input"], template=template)

ollama_llm = Ollama(model=os.getenv("OLLAMA_MODEL"))
# Interaction function for user input
def interact_with_bot(user_input):
    try:
        # Pass user input into the model and generate a response
        return ollama_llm(prompt.format(input=user_input))
    except Exception as e:
        # Handle any errors and prevent them from showing in the prompt
        return "Sorry, I couldn't process that request."

# Main loop to simulate user-bot interaction
if __name__ == "__main__":
    print("Chat with the bot! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        bot_response = interact_with_bot(user_input)
        print(f"Bot: {bot_response}")
