from agno.agent import Agent, RunOutput
import models as m


agent = Agent(
    name="Basic Agent",
    model=m.default,
)

q = "share a 2 sentence horror story"

r: RunOutput = agent.run(q)
print(r.content)

# agent.print_response(q)
