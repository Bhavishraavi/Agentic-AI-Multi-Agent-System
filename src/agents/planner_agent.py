from typing import Dict, Any
from src.agents.tool_agent import tool_agent




def planner_agent(state: Dict[str, Any]):
    task = state["task"]       # FIXED
    response = agent_respond(f"Plan the steps to solve: {task}")
    return {"plan": response}




