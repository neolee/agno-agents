from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.googlesearch import GoogleSearchTools
import mal.agno.model as model


m = model.default

agent = Agent(
    name="DuckDuckGo Agent",
    model=m,
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

q = "Tell me about NVIDIA's Digits computer"
agent.print_response(q)

agent = Agent(
    name="Google Agent",
    model=m,
    tools=[GoogleSearchTools()],
    description="你是一个新闻文章智能体，帮助用户获得最新的新闻资料",
    instructions=[
        "对用户的每个查询主题提供4篇最新的相关新闻报道，",
        "搜索最新的10篇报道并选取里面排名最高的4篇非重复的内容，",
        "所搜所有中文和英文的内容。",
    ],
    show_tool_calls=True,
    markdown=True,
    # debug_mode=True,
)

q = "告诉我俄乌战争的最新进展"
agent.print_response(q)
