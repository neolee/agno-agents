from agno.agent.agent import Agent
from agno.tools.crawl4ai import Crawl4aiTools
import mal.agno.model as model


agent = Agent(
    model=model.default,
    tools=[Crawl4aiTools(max_length=None)],
    show_tool_calls=True,
    markdown=True,
)

# url = "https://www.news.cn/politics/20250119/f33c2caa323249ca8fd2038515ee9620/c.html"
url = "https://ysymyth.github.io/The-Second-Half/"

# prompt = "Tell me about "
prompt = "阅读网页并给出内容摘要："

agent.print_response(prompt + url, stream=True)
