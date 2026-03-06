from agents.state import ResumeTailorState


def decision_agent(state: ResumeTailorState):
    
    state["agent_step"] = "Decision Agent"
    state["progress"] = 60

    # print("\n===== Decision Agent START =====")

    similarity_score = state.get("similarity_score", 0)
    missing_skills = state.get("missing_skills", [])
    matched_skills = state.get("matched_skills", [])

    # print("Similarity Score:", similarity_score)
    # print("Matched Skills:", matched_skills)
    # print("Missing Skills:", missing_skills)

    # Decision logic
    if similarity_score >= 80 and len(missing_skills) <= 2:
        state["should_tailor"] = False
        # print("Decision: Tailoring NOT required.")
        # print("Reason: High similarity and minimal skill gap.")
    else:
        state["should_tailor"] = True
        # print("Decision: Tailoring required.")
        # print("Reason: Resume could be better aligned with JD.")

    # print("===== Decision Agent END =====\n")

    return state