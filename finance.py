from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
import models as m


agent = Agent(
    name="Finance Agent",
    model=m.default,
    tools=[YFinanceTools()],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True
)

q = "Summarize analyst recommendations for NVDA"

agent.print_response(q, stream=True)
