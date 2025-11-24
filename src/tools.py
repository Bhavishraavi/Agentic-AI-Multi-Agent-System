import os
import traceback
from dotenv import load_dotenv
import requests

load_dotenv()

# ---------------------------------------------------
# 🔢 CALCULATOR TOOL
# ---------------------------------------------------
def calculator_tool(query: str):
    """
    Performs math calculations.
    Example: "calculate 45 * 98"
    """
    try:
        expr = query.lower().replace("calculate", "").strip()
        result = eval(expr)
        return f"Result: {result}"
    except Exception as e:
        return f"Calculator error: {e}"

# ---------------------------------------------------
# 🐍 PYTHON EXECUTION TOOL
# ---------------------------------------------------
def python_tool(code: str):
    """
    Runs Python code in a restricted environment.
    Example: "python: for i in range(5): print(i)"
    """
    try:
        local_vars = {}
        exec(code, {}, local_vars)
        return str(local_vars) if local_vars else "Python executed successfully."
    except Exception as e:
        return f"Python execution error:\n{traceback.format_exc()}"

# ---------------------------------------------------
# 📄 FILE READER TOOL
# ---------------------------------------------------
def read_file_tool(filename: str):
    """
    Reads a local file (txt or md).
    Note: PDF reading is handled in rag.py.
    """
    filename = filename.strip()

    if not os.path.exists(filename):
        return f"File not found: {filename}"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"File read error: {e}"

# ---------------------------------------------------
# 🌐 WEB SEARCH TOOL (TAVILY)
# ---------------------------------------------------
def search_tool(query: str):
    """
    Performs web search using Tavily API.
    Requires TAVILY_API_KEY in .env
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return "Tavily API key not found. Add TAVILY_API_KEY to .env."

    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={"query": query, "max_results": 3},
            headers={"Authorization": f"Bearer {api_key}"}
        )
        data = response.json()
        results = data.get("results", [])
        formatted = "\n".join([f"- {r['content']} ({r['url']})" for r in results])
        return formatted if formatted else "No results found."
    except Exception as e:
        return f"Web search error: {e}"

# ---------------------------------------------------
# 🔧 TOOL ROUTER — CHOOSES THE TOOL
# ---------------------------------------------------
def tool_router(query: str):
    """
    Simple rule-based tool selector.
    You can upgrade it later to an LLM-based router.
    """

    q = query.lower()

    # Calculator
    if any(x in q for x in ["calculate", "+", "-", "*", "/", "%", "math"]):
        return calculator_tool(query)

    # Python run
    if "python:" in q:
        code = query.split("python:", 1)[1]
        return python_tool(code)

    # File reader
    if "read file" in q:
        filename = q.replace("read file", "").strip()
        return read_file_tool(filename)

    # Web search
    if any(x in q for x in ["search", "google", "find this", "who is", "what is"]):
        return search_tool(query)

    return "No matching tool found."
