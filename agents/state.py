from typing import TypedDict, List, Optional


class ResumeTailorState(TypedDict):

    # User inputs
    resume_text: str
    job_description: str

    # Extracted resume information
    resume_skills: List[str]
    resume_tools: List[str]
    resume_role: Optional[str]

    # Extracted job description information
    jd_required_skills: List[str]
    jd_preferred_skills: List[str]
    jd_role: Optional[str]

    # Matching outputs
    matched_skills: List[str]
    missing_skills: List[str]
    similarity_score: Optional[float]
    
    # Tailoring decision
    should_tailor: bool
    
    # Project selection
    use_project_library: bool
    selected_projects: list

    # Final generation
    tailored_resume: Optional[str]
    
    # UI tracking
    agent_step: Optional[str]
    progress: Optional[str]
