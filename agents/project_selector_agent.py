from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
from agents.state import ResumeTailorState

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def project_selector_agent(state: ResumeTailorState):
    
    state["agent_step"] = "Project Selector"
    state["progress"] = 75

    # print("\n===== Project Selector Agent START =====")

    # Check if project library is enabled
    use_project_library = state.get("use_project_library", False)

    if not use_project_library:
        # print("Project library disabled — skipping project selection.")
        state["selected_projects"] = []
        # print("===== Project Selector Agent END =====\n")
        return state

    # Load projects.json
    try:
        with open("data/projects.json", "r") as f:
            project_data = json.load(f)["projects"]
    except Exception as e:
        # print("Project selection unavailable:", e)
        state["selected_projects"] = []
        # print("===== Project Selector Agent END =====\n")
        return state

    # print(f"Loaded {len(project_data)} projects from library")

    # Build JD text
    jd_text = " ".join(state.get("jd_required_skills", [])) + " " + state.get("job_description", "")

    jd_embedding = model.encode(jd_text)

    scored_projects = []

    # semantic similarity for scoring
    for project in project_data:

        project_text = (
            project.get("name", "") +
            " " +
            project.get("description", "") +
            " " +
            " ".join(project.get("skills", []))
        )

        project_embedding = model.encode(project_text)

        similarity = cosine_similarity(
            [jd_embedding],
            [project_embedding]
        )[0][0]

        scored_projects.append({
            "project": project,
            "score": similarity
        })

    # Sort projects by score
    scored_projects.sort(key=lambda x: x["score"], reverse=True)

    # Keep only projects with relevance
    relevant_projects = [p for p in scored_projects if p["score"] > 0]

    # Select top 3
    selected_projects = [p["project"] for p in relevant_projects[:3]]
    
    # Save into state
    state["selected_projects"] = selected_projects
    
    # # final selected projects:
    # if selected_projects:
    #     print("Selected Projects:")
    #     for p in selected_projects:
    #         print("-", p["name"])
    # else:
    #     print("No relevant projects found.")

    # print("===== Project Selector Agent END =====\n")

    return state