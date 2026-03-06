from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_skill_gap(jd_data, resume_data):

    jd_skills = (
        jd_data.get("required_skills", [])
        + jd_data.get("preferred_skills", [])
        + jd_data.get("tools_technologies", [])
    )

    resume_skills = (
        resume_data.get("skills", [])
        + resume_data.get("tools_technologies", [])
    )

    if not jd_skills or not resume_skills:
        return {"matched_skills": [], "missing_skills": []}

    jd_embeddings = model.encode(jd_skills)
    resume_embeddings = model.encode(resume_skills)

    matched = []
    missing = []

    for i, jd_skill in enumerate(jd_skills):

        similarities = cosine_similarity(
            [jd_embeddings[i]],
            resume_embeddings
        )[0]

        if max(similarities) >= 0.65:
            matched.append(jd_skill)
        else:
            missing.append(jd_skill)

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }