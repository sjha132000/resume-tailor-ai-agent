from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# def compute_match_score(resume_text, jd_text):

#     resume_emb, jd_emb = model.encode([resume_text, jd_text])

#     score = cosine_similarity([resume_emb], [jd_emb])[0][0]

#     return round(score * 100, 2)


def compute_match_score(resume_skills, jd_skills):

    # Ensure inputs are strings
    if isinstance(resume_skills, list):
        resume_text = " ".join(resume_skills)
    else:
        resume_text = resume_skills

    if isinstance(jd_skills, list):
        jd_text = " ".join(jd_skills)
    else:
        jd_text = jd_skills

    embeddings = model.encode([resume_text, jd_text])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(similarity * 100, 2)