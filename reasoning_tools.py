from textwrap import dedent

from agno.agent.agent import Agent
from agno.tools.thinking import ThinkingTools
from agno.tools.yfinance import YFinanceTools

import mal.agno.model as model


thinking_agent = Agent(
    model=model.default,
    tools=[
        ThinkingTools(),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    instructions=dedent("""\
    ## Using the think tool
    Before taking any action or responding to the user after receiving tool results, use the think tool as a scratchpad to:
    - List the specific rules that apply to the current request
    - Check if all required information is collected
    - Verify that the planned action complies with all policies
    - Iterate over tool results for correctness

    ## Rules
    - Its expected that you will use the think tool generously to jot down thoughts and ideas.
    - Use tables where possible\
    """),
    show_tool_calls=True,
)

thinking_agent.print_response(
    "Write a report comparing NVDA to TSLA", stream=True, markdown=True
)
