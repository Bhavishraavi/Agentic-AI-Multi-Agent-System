from src.agents.planner_agent import planner_agent
from src.agents.tool_agent import tool_agent
from src.agents.researcher_agent import researcher_agent
from src.agents.answer_agent import answer_agent
from src.agents.respond_agent import agent_respond

def build_graph():
    return {
        "planner": planner_agent,
        "tool": tool_agent,
        "researcher": researcher_agent,
        "answer": answer_agent,
        "respond": agent_respond
    }


