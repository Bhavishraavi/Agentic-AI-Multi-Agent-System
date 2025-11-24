from typing import Dict, Any
from src.agents.respond_agent import agent_respond


def researcher_agent(state: Dict[str, Any]):
    task = state["task"]       # FIXED
    response = agent_respond(f"Research about: {task}")
    return {"research": response}

