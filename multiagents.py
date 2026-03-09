from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

web_agent=Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="gemma2-9b-it"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="gemma2-9b-it"),
    tools=[YFinanceTools()],
    instructions="Use tables to display data",
    markdown=True,
)

multi_agent=Agent(
    model=Groq(id="gemma2-9b-it"),
    tools=[DuckDuckGoTools()],
    instructions="You are a financial analyst. Search for recent stock performance, news, and analysis of Tesla, Nvidia, and Apple. Provide a clear investment recommendation based on current market conditions.",
    markdown=True,
)

multi_agent.print_response("Search for recent stock performance and news about Tesla, Nvidia, and Apple. Which stock should I buy for maximum profits based on current market conditions?")
