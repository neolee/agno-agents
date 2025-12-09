from agno.agent import Agent
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import models as m


web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=m.default,
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=m.default,
    tools=[YFinanceTools()],
    instructions=["Use tables to display data"],
    markdown=True,
)

agent_team = Team(
    model=m.default,
    members=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    markdown=True,
)

q = "Summarize analyst recommendations for NVDA then search for the latest news about NVIDIA"

agent_team.print_response(q, stream=True)
