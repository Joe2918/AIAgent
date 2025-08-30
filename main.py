import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


def main():    
    load_dotenv()
    args = sys.argv[1:]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    is_verbose = False
    if args[-1] == "--verbose":
        print(f"User prompt: {user_prompt}")
        is_verbose = True

    generate_content(client, messages, is_verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print("Response:")
    print(response.text)

    

if __name__ == "__main__":
    main()