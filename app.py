import streamlit as st
from graph.workflow import build_graph
from utils.parser import extract_text_from_pdf


st.set_page_config(page_title="AI Resume Tailor Agent")

st.title("AI Resume Tailor Agent")

st.write("Tailor your resume intelligently using AI agents.")

# ---- Upload Resume & JD ----
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description Here", height=250)

# ---- Project library toggle ----
use_project_library = st.checkbox("Use Project Library (Optional)")

generate_button = st.button("Generate Tailored Resume")

if generate_button:

    if not resume_file or not job_description:
        st.warning("Please upload resume and paste job description.")
    else:
        with st.spinner("Analyzing..."):

            resume_text = extract_text_from_pdf(resume_file)

            graph = build_graph()

            state = {
                "resume_text": resume_text,
                "job_description": job_description,
                "use_project_library": use_project_library
            }

            progress_bar = st.progress(0)
            status_text = st.empty()

            result = graph.invoke(state)

            progress_bar.progress(100)
            status_text.success("All agents completed")

        st.success("Analysis Complete")

        # # ---- Display Results ----
        # st.success("Analysis Complete")

        # # ---------- MATCH SCORE ----------
        # st.subheader("Similarity Score")
        # if "similarity_score" in result:
        #     score = result["similarity_score"]
        #     st.metric("Match Score", f"{score:.2f}%")
        #     st.progress(score / 100)
        
        # ---- Extract Results ----
        similarity_score = result.get("similarity_score", 0)
        matched_skills = result.get("matched_skills", [])
        missing_skills = result.get("missing_skills", [])
        tailored_resume = result.get("tailored_resume", "")
        
        # ---- Agent Execution Progress ----
        st.subheader("Agent Execution")

        agents = [
            "Resume Agent",
            "JD Agent",
            "Matcher Agent",
            "Decision Agent",
            "Project Selector",
            "Tailor Agent"
        ]
        
        for agent in agents:
            st.write(f"✔ {agent}")

        # current_agent = result.get("agent_step", "")

        # for agent in agents:
        #     if agent == current_agent:
        #         st.write(f"🔄 {agent} running")
        #     else:
        #         st.write(f"✔ {agent} completed")
        

        # ---------- ATS SCORE ----------
        st.subheader("Resume Match")

        st.metric("Similarity Score", f"{similarity_score:.2f}%")

        st.progress(float(similarity_score) / 100)

        if similarity_score >= 80:
            st.success("Strong ATS alignment")
        elif similarity_score >= 60:
            st.warning("Moderate alignment — tailoring recommended")
        else:
            st.error("Low alignment — resume needs improvement")
        
        # ---------- SKILL ALIGNMENT ----------
        st.subheader("Skill Alignment")
        
        col1, col2 = st.columns(2)
        
        def render_skill_bubbles(skills, color, icon, empty_message):

            if skills:
                bubbles = "<div style='display:flex; flex-wrap:wrap;'>"

                for skill in skills:
                    bubbles += (
                        f"<span style='background-color:{color}; "
                        f"padding:6px 14px; "
                        f"border-radius:20px; "
                        f"margin:6px; "
                        f"font-size:14px; "
                        f"border:1px solid rgba(255,255,255,0.08);'>"
                        f"{icon} {skill}</span>"
                    )

                bubbles += "</div>"

                st.markdown(bubbles, unsafe_allow_html=True)

            else:
                st.info(empty_message)

        with col1:
            st.markdown("### Matched Skills")
            render_skill_bubbles(
                matched_skills,
                "#123524",
                "✔",
                "No strong skill matches detected"
            )

        with col2:
            st.markdown("### Missing Skills")
            render_skill_bubbles(
                missing_skills,
                "#3b1f1f",
                "✖",
                "No major skill gap found"
            )

        # ---------- TAILORED RESUME ----------
        st.subheader("Tailored Resume")
        st.text_area("Rewritten Resume (Editable)", tailored_resume, height=450)

        # edited_resume = st.text_area("Rewritten Resume (Editable)", tailored_resume, height=450)

        # st.download_button("Download Resume", edited_resume, file_name="tailored_resume.doc")