from agents.state import ResumeTailorState
from utils.matcher import compute_match_score
from utils.skill_gap import compute_skill_gap


def matcher_agent(state: ResumeTailorState):
    
    state["agent_step"] = "Matcher Agent"
    state["progress"] = 45
    
    # print("\n===== Matcher Agent START =====")

    resume_data = {
        "skills": state.get("resume_skills", []),
        "tools_technologies": state.get("resume_tools", [])
    }

    jd_data = {
        "required_skills": state.get("jd_required_skills", []),
        "preferred_skills": state.get("jd_preferred_skills", [])
    }
    
    # print("Resume Skills:", resume_data["skills"])
    # print("JD Required Skills:", jd_data["required_skills"])

    similarity_score = compute_match_score(
        resume_data["skills"],
        jd_data["required_skills"]
    )

    gap_result = compute_skill_gap(jd_data, resume_data)

    state["similarity_score"] = similarity_score
    state["matched_skills"] = gap_result["matched_skills"]
    state["missing_skills"] = gap_result["missing_skills"]
    
    # print("Similarity Score:", similarity_score)
    # print("Matched Skills:", state["matched_skills"])
    # print("Missing Skills:", state["missing_skills"])
    
    # print("===== Matcher Agent END =====\n")

    return state