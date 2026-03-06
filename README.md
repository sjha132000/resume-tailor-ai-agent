# AI Resume Tailor Agent

An AI-powered **multi-agent system** that analyzes a resume against a job
description, evaluates skill alignment, computes an ATS-style similarity
score, and generates a tailored resume optimized for the target role.

The system uses LLMs for structured information extraction and
rewriting, along with semantic embeddings for skill matching. The
workflow is implemented using **LangGraph**, enabling specialized agents to
collaboratively analyze resumes, evaluate alignment, and generate
improvements.

The interface is built with **Streamlit**, allowing users to upload a
resume, paste a job description, and receive structured analysis along
with a tailored resume.

------------------------------------------------------------------------

## Project Structure

```
resume-tailor-ai-agent/
│
├── app.py
│
├── agents/
│   ├── state.py
│   ├── resume_agent.py
│   ├── jd_agent.py
│   ├── matcher_agent.py
│   ├── decision_agent.py
│   ├── project_selector_agent.py
│   └── tailor_agent.py
│
├── graph/
│   └── workflow.py
│
├── utils/
│   ├── parser.py
│   ├── matcher.py
│   ├── tailor.py
│   ├── llm.py
│   ├── skill_gap.py
│   ├── jd_analyzer.py
│   └── resume_analyzer.py
│
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

**File roles**

`app.py`: Streamlit user interface

`state.py`: Defines the shared state object used by agents to pass data across the workflow

`resume_agent.py`: Extracts skills and tools from the resume

`jd_agent.py`: Extracts required and preferred skills from job descriptions

`matcher_agent.py`: Computes semantic similarity and ATS alignment score

`decision_agent.py`: Determines whether resume tailoring is necessary

`project_selector_agent.py`: Selects relevant projects based on job relevance

`tailor_agent.py`: Generates a tailored resume aligned with the job description

`workflow.py`: Defines the LangGraph multi-agent pipeline

`parser.py`: Extracts text from PDF resumes

`matcher.py`: Implements semantic similarity using embeddings

`tailor.py`: Resume rewriting logic using LLMs

`llm.py`: Interface for interacting with the LLM (Gemini API)

`skill_gap.py`: Identifies matched and missing skills between the resume and job description

`jd_analyzer.py`: Structured job description analysis

`resume_analyzer.py`: Structured resume analysis

------------------------------------------------------------------------

## Architecture

The system follows a **multi-agent architecture** where each agent performs a
specific stage of the resume optimization pipeline. Each agent receives a
shared state object, updates it with new information, and passes it to the
next agent in the workflow.

```
Resume PDF
    │
    ▼
parser.py
    │
    ▼
Resume Agent
    │
    ▼
JD Agent
    │
    ▼
Matcher Agent
    │
    ▼
Decision Agent
    │
    ▼
Project Selector Agent
    │
    ▼
Tailor Agent
    │
    ▼
Streamlit UI
```

------------------------------------------------------------------------

# Tech Stack

Frontend / Interface - Streamlit

AI / LLM - Gemini API

Agent Framework - LangGraph

NLP & Semantic Matching - Sentence Transformers - MiniLM embeddings

Supporting Libraries - Scikit-learn - PDFPlumber - Python Dotenv

------------------------------------------------------------------------

# Installation

## 1. Clone the repository

``` bash
git clone https://github.com/sjha132000/resume-tailor-ai-agent.git 
cd resume-tailor-ai-agent
```

------------------------------------------------------------------------

## 2. Create a virtual environment

``` bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

``` bash
.venv\Scripts\activate
```

------------------------------------------------------------------------

## 3. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 4. Environment setup

Create a `.env` file in the root directory and add API key:

``` bash
GEMINI_API_KEY=your_api_key_here
```

------------------------------------------------------------------------

## 5. Run the application

``` bash
streamlit run app.py
```

The application will launch locally at:

    http://localhost:8501
