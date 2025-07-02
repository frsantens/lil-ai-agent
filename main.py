import os
import sys
from config import system_prompt
from functions.get_files_info import schema_get_files_info
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

    if len(sys.argv) == 1:
        print("Usage: python main.py <prompt> [--verbose]")
        sys.exit(1)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
            ),
    )

    if "--verbose" in sys.argv:
        print(f"User prompt: {sys.argv[1]}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    if response.function_calls:
        for function_call_part in response.function_calls: 
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print("Response:")
        print(response.text)

if __name__ == "__main__":
    main()
