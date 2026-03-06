from utils.llm import generate_response
import json
import re

def clean_json_output(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text.strip()

def analyze_job_description(model_name: str, job_description: str):

    prompt = f"""
You are an expert recruitment analyst.

Extract structured information from the job description below.

Return ONLY valid JSON.
Do NOT include markdown formatting.
Do NOT wrap the output in triple backticks.

Format:

{{
  "role_type": "",
  "seniority_level": "",
  "required_skills": [],
  "preferred_skills": [],
  "tools_technologies": [],
  "key_action_verbs": []
}}

Job Description:
{job_description}
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