from utils.llm import generate_response
import json
import re

def clean_json_output(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text.strip()

def analyze_resume(model_name: str, resume_text: str):

    prompt = f"""
You are an expert resume parser.

Extract structured information from the resume below.

Return ONLY valid JSON.
Do NOT include markdown formatting.

Format:

{{
  "candidate_role_profile": "",
  "skills": [],
  "tools_technologies": [],
  "key_action_verbs": []
}}

Resume:
{resume_text}
"""

    response = generate_response(model_name, prompt)
    cleaned = clean_json_output(response)

    try:
        return json.loads(cleaned)
    except:
        return {
            "error": "Model did not return valid JSON.",
            "raw_output": response
        }