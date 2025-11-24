from typing import Dict, Any
from src.agents.respond_agent import agent_respond


def answer_agent(state: Dict[str, Any]):
    task = state["task"]       # FIXED
    response = agent_respond(f"Final answer for: {task}")
    return {"answer": response}

