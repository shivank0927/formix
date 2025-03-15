import os
import sys
# from args import Fetcher # args pos argument.
from google import genai

def integration(lang, arch):
    client = genai.Client(api_key=os.getenv("Api_Key"))

    PROMPT_PATH = os.path.abspath("prompts/prompt.txt")
    print(PROMPT_PATH)

    with open(PROMPT_PATH, "r") as prompt:
        content = prompt.read()
    content = content.replace("{language}", lang).replace("{architecture}", arch)
    if content:
        print("creating response...")
    else:
        sys.exit("integrate file error")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=content
    )
    return response.text

if __name__=="__main__":
    integration()