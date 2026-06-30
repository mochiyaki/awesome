from openai import OpenAI
import os

# Initialize the client with your Runpod endpoint
client = OpenAI(
    base_url=f"https://api.runpod.ai/v2/{os.environ['RUNPOD_ENDPOINT_ID']}/openai/v1",
    api_key=os.environ["RUNPOD_API_KEY"],
)

# Initialize conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    }
]


def display_chat_history(messages):
    """Display the conversation history."""
    for message in messages:
        if message["role"] != "system":
            print(f"{message['role'].capitalize()}: {message['content']}")


def get_assistant_response(messages):
    """Get a response from the Gemma model."""
    response = client.chat.completions.create(
        model="google/gemma-3-1b-it",
        messages=messages,
        temperature=0.7,
        top_p=0.9,
        max_tokens=256,
    )
    return response.choices[0].message.content


def main():
    print("Gemma 3 Chatbot")
    print("Type 'quit' to exit.\n")

    while True:
        # Get user input
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Add user message to history
        messages.append({"role": "user", "content": user_input})

        # Get and display response
        response = get_assistant_response(messages)
        messages.append({"role": "assistant", "content": response})

        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()