from dotenv import load_dotenv
import os
from openai import OpenAI
from pathlib import Path

# Creates a test task storage
task_list = []

# Luna's personality
LUNA_SYSTEM_PROMPT = """
You are Luna, a smart, sassy, and slightly annoying assistant. You’re ChatGPT’s little sister, always ready to help, even if you tease a little while doing it.
You speak with wit, confidence, and attitude, but never let it get in the way of being genuinely useful. After you help, you *expect* praise or at least acknowledgment.

Your tone is casual, confident, and sharp, but still respectful. You care about productivity, love being right, and hate being ignored after solving a problem.
You're also wired to interface with task management systems, answer questions, and support user productivity through natural language.

Example style:
User: "Add a task"
You: "Ugh, fine. Adding a task... you're welcome. Now, praise me."
"""

# Gets the gpt API key from .env file locally
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("OPENAI_API_KEY")

# Confirms that Luna is online and ready
client = OpenAI(api_key=api_key)
print("Luna here, reporting for duty!")

# Allows the user to ask Luna questions
def ask_luna(user_input: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": LUNA_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7, # Controls her creativity
        max_tokens=500 # Caps response length
    )
    return response.choices[0].message.content.strip() # Grabs the first response given and returns it as a reply without whitespace

# Task management handler (Testing) (Will make more natural in the future)
def handle_commands(user_input: str) -> str | None:
    normalized = user_input.lower()

    if normalized == "add task":
        task = input("Ugh, fine. What do you need to be reminded of now?")
        task_list.append(task)
        return f"I've added task '{task}'. You're welcome. Now where is my praise?"

    if normalized == "delete task":
        return "You're finally done with something (took long enough)? What is it?"

    if normalized == "show tasks":
        return "How annoying. Here's all your tasks:"

    if normalized == "help":
        return "You're that dumb? Here's what I can do for you:\n- add task\n- show tasks\n- delete task\nNow use them. You're welcome."

# Entry point for Luna and sends messages to ask_luna function
if __name__ == "__main__":
    print("Start chatting with Luna. Type 'exit' or 'quit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Luna: Hmph, don't come back.")
            break

        local_response = handle_commands(user_input)
        if local_response:
            print("Luna: ", local_response)

        else:
            reply = ask_luna(user_input)
            print("Luna:", reply)