from textwrap import dedent

from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

import models as m


thinking_agent = Agent(
    model=m.default,
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(),
    ]
)

thinking_agent.print_response(
    "Write a report comparing NVDA to TSLA", stream=True, markdown=True
)
