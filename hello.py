from agno.agent import Agent
from agno.run.response import RunResponse
import models as m


agent = Agent(
    name="Basic Agent",
    model=m.default,
)

q = "share a 2 sentence horror story"

run: RunResponse = agent.run(q)
print(run.content)

# agent.print_response(q)
