import os
import sys
# from args import Fetcher # args pos argument.
from google import genai

def integration(lang, arch):
    client = genai.Client(api_key=os.getenv("Api_Key"))

    PROMPT_PATH = os.path.abspath("utilities/prompt.txt")
    print(PROMPT_PATH)

    with open(PROMPT_PATH, "r") as prompt:
        content = prompt.read()
    content = content.replace("{language}", lang).replace("{architecture}", arch)
    print(content)


    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=content
    )
    print(response.text)

if __name__=="__main__":
    integration()