from agno.agent.agent import Agent
from agno.tools.yfinance import YFinanceTools
import mal.agno.model as model


agent = Agent(
    name="Finance Agent",
    model=model.default,
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

q = "Summarize analyst recommendations for NVDA"

agent.print_response(q, stream=True)
