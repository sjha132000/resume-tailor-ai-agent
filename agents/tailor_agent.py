from agents.state import ResumeTailorState
from utils.tailor import generate_tailored_resume


def tailor_agent(state: ResumeTailorState):
    
    state["agent_step"] = "Tailor Agent"
    state["progress"] = 95
    
    # print("\n===== Tailor Agent START =====")
    
    should_tailor = state.get("should_tailor", True)
    # similarity_score = state.get("similarity_score", 0)
    
    # print("Similarity Score:", similarity_score)
    # print("Should Tailor:", should_tailor)

    if not should_tailor:
        # print("Skipping tailoring — resume already well aligned.")
        state["tailored_resume"] = state["resume_text"]

        # print("===== Tailor Agent END =====\n")
        return state

    resume_text = state["resume_text"]
    
    jd_data = {
        "role_type": state.get("jd_role"),
        "required_skills": state.get("jd_required_skills", []),
        "preferred_skills": state.get("jd_preferred_skills", [])
    }
    
    skill_gap_data = {
        "matched_skills": state.get("matched_skills", []),
        "missing_skills": state.get("missing_skills", []),
    }
    
    selected_projects = state.get("selected_projects", [])
    
    # print("Matched Skills:", skill_gap_data["matched_skills"])
    # print("Missing Skills:", skill_gap_data["missing_skills"])
    
    # if selected_projects:
    #     print("\nSelected Projects from Library:")
    #     for p in selected_projects:
    #         print("-", p["name"])
    # else:
    #     print("\nNo additional projects selected from library.")

    tailored_resume = generate_tailored_resume(
        "gemini", 
        resume_text, 
        jd_data, 
        skill_gap_data, 
        selected_projects
    )

    state["tailored_resume"] = tailored_resume
    
    # print("Tailored resume generated successfully.")
    
    # print("===== Tailor Agent END =====\n")
    
    state["progress"] = 100

    return state