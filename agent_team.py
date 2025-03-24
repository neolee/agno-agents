from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import mal.agno.model as model


m = model.ollama

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=m,
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=m,
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         company_info=True,
                         company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=m,
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

q = "Summarize analyst recommendations for NVDA then search for the latest news about NVIDIA"

agent_team.print_response(q, stream=True)
