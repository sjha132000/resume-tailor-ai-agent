from agents.state import ResumeTailorState
from utils.resume_analyzer import analyze_resume


def resume_agent(state: ResumeTailorState):
    
    state["agent_step"] = "Resume Agent"
    state["progress"] = 10
    
    # print("\n===== Resume Agent START =====")

    resume_text = state["resume_text"]
    # print("Input resume_text:", resume_text[:80], "...")

    # reuse your existing analyzer
    result = analyze_resume("gemini", resume_text)

    state["resume_skills"] = result.get("skills", [])
    state["resume_tools"] = result.get("tools_technologies", [])
    state["resume_role"] = result.get("candidate_role_profile", "")
    
    # print("Extracted resume_skills:", state["resume_skills"])
    # print("Extracted resume_tools:", state["resume_tools"])
    
    # print("===== Resume Agent END =====\n")

    return state