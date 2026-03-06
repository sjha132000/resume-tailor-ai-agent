from graph.workflow import build_graph

graph = build_graph()

state = {
    "resume_text": "I built machine learning models using Python and AWS",
    "job_description": "Looking for a data scientist skilled in Python, SQL, and machine learning",
    "use_project_library": True
}

result = graph.invoke(state)

print(result)