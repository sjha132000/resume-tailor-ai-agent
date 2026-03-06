from langgraph.graph import StateGraph, END

from agents.state import ResumeTailorState
from agents.resume_agent import resume_agent
from agents.jd_agent import jd_agent
from agents.matcher_agent import matcher_agent
from agents.decision_agent import decision_agent
from agents.project_selector_agent import project_selector_agent
from agents.tailor_agent import tailor_agent


def build_graph():

    workflow = StateGraph(ResumeTailorState)

    # Add nodes
    workflow.add_node("resume_agent", resume_agent)
    workflow.add_node("jd_agent", jd_agent)
    workflow.add_node("matcher_agent", matcher_agent)
    workflow.add_node("decision_agent", decision_agent)
    workflow.add_node("project_selector_agent", project_selector_agent)
    workflow.add_node("tailor_agent", tailor_agent)

    # Define execution order
    workflow.set_entry_point("resume_agent")

    workflow.add_edge("resume_agent", "jd_agent")
    workflow.add_edge("jd_agent", "matcher_agent")
    workflow.add_edge("matcher_agent", "decision_agent")
    workflow.add_edge("decision_agent", "project_selector_agent")
    workflow.add_edge("project_selector_agent", "tailor_agent")

    workflow.add_edge("tailor_agent", END)

    return workflow.compile()