from agents.state import ResumeTailorState
from utils.jd_analyzer import analyze_job_description


def jd_agent(state: ResumeTailorState):
    
    state["agent_step"] = "JD Agent"
    state["progress"] = 25
    
    # print("\n===== JD Agent START =====")

    job_description = state["job_description"]
    # print("Input job_description:", job_description[:80], "...")

    result = analyze_job_description("gemini", job_description)

    state["jd_required_skills"] = result.get("required_skills", [])
    state["jd_preferred_skills"] = result.get("preferred_skills", [])
    state["jd_role"] = result.get("role_type", "")
    
    # print("JD Required Skills:", state["jd_required_skills"])
    # print("JD Preferred Skills:", state["jd_preferred_skills"])
    
    # print("===== JD Agent END =====\n")

    return state