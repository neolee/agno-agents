from agno.agent.agent import Agent
from agno.run.response import RunResponse
import mal.agno.model as model


agent = Agent(
    name="Basic Agent",
    model=model.default,
)

q = "share a 2 sentence horror story"

run: RunResponse = agent.run(q)
print(run.content)

# agent.print_response(q)
