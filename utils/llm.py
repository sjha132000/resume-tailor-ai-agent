import os
# import ollama
from google import genai
from dotenv import load_dotenv

load_dotenv()

def generate_response(model_name: str, prompt: str):

    # if model_name == "llama":
    #     response = ollama.chat(
    #         model="llama3",
    #         messages=[{"role": "user", "content": prompt}]
    #     )
    #     return response["message"]["content"]

    if model_name == "gemini":
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    else:
        raise ValueError("Unsupported model selected.")