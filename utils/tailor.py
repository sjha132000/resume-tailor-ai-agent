from utils.llm import generate_response

def generate_tailored_resume(
    model_name,
    resume_text,
    jd_data,
    skill_gap_data,
    selected_projects
):
    
    # Build projects section separately
    projects_section = ""

    if selected_projects:
        # formatted_projects = "\n".join(
        #     [f"- {p['name']}: {p.get('description','')}" for p in selected_projects]
        # )
        formatted_projects = "\n".join(
            [
                f"- {p['name']}: {p.get('description','')}"
                if isinstance(p, dict)
                else f"- {p}"
                for p in selected_projects
            ]
)

        projects_section = f"""
Additional candidate projects that may be included if relevant to the job:

{formatted_projects}
"""

    prompt = f"""
You are an expert resume editor.

Your task:
Rewrite the resume to better align with the job description.

STRICT RULES:
- Do NOT invent company names.
- Do NOT add new roles.
- Do NOT fabricate metrics or outcomes.
- Do NOT add years or dates.
- Only rewrite the provided content.
- Emphasize matched skills.
- If a missing skill is already implied, make it clearer.
- Keep formatting clean and professional.
- Only include additional projects if they improve alignment with the job description.
- Keep the resume concise and suitable for a one-page format.

Job Role: {jd_data.get("role_type")}
Required Skills: {jd_data.get("required_skills")}
Preferred Skills: {jd_data.get("preferred_skills")}
Missing Skills: {skill_gap_data.get("missing_skills")}
Matched Skills: {skill_gap_data.get("matched_skills")}

{projects_section}

Original Resume:
{resume_text}

Return:
1. Professional Summary (rewritten)
2. Experience Section (rewritten as bullet points)
3. Projects Section (rewrite existing projects and optionally include relevant additional projects)
"""

    return generate_response(model_name, prompt)