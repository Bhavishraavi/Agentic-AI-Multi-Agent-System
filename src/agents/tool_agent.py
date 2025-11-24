from typing import Any, Dict
from src.agents.respond_agent import agent_respond


def tool_agent(state: Dict[str, Any]):
    task = state["task"]       # FIXED
    return {"tools": f"Tool executed for: {task}"}


