import os
import sys
from google import genai

def integration(language, architecture, api_key):
    try:
        client = genai.Client(api_key=api_key)

        PROMPT_PATH = os.path.abspath("prompts/prompt.txt")
        print(PROMPT_PATH)

        with open(PROMPT_PATH, "r") as prompt:
            content = prompt.read()

        content = content.replace("{language}", language).replace("{architecture}", architecture)
        
        if not content:
            sys.exit("integrate file error")

        print("creating response...")

        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=[{"text": content}]
        )
        
        print (response.text)
        
        return response.text if response else None
    
    except Exception as e:
        sys.exit(f"{e}")

if __name__ == "__main__":
    sys.exit("")
