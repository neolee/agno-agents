from agno.agent.agent import Agent
from agno.tools.crawl4ai import Crawl4aiTools
import mal.agno.model as model


agent = Agent(
    model=model.default,
    tools=[Crawl4aiTools(max_length=None)],
    show_tool_calls=True,
    markdown=True,
)


if __name__ == "__main__":
    prompt = "阅读网页并给出内容摘要："
    url = "https://ysymyth.github.io/The-Second-Half/"

    import argparse
    parser = argparse.ArgumentParser(description="web crawler agent")
    parser.add_argument("url", type=str, help="url to read", nargs='?')
    args = parser.parse_args()
    if args.url: url = args.url

    agent.print_response(prompt + url, stream=True)
