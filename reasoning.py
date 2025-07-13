from agno.agent.agent import Agent
import models as m


def reasoning(task: str):
    reasoning_agent = Agent(
        model=m.default,
        reasoning_model=m.default_reasoner
    )

    reasoning_agent.print_response(task, stream=True)


if __name__ == "__main__":
    task = "8.11 and 8.9 -- which is bigger?"

    reasoning(task)
