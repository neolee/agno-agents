from typing import List
from rich.pretty import pprint
from pydantic import BaseModel, Field
from agno.agent.agent import Agent
from agno.run.response import RunResponse
import mal.agno.model as model


# pydantic model to enforce the structure of the output
class MovieScript(BaseModel):
    setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
    ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
    genre: str = Field(..., description="Genre of the movie. If not available, select action, thriller or romantic comedy.")
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")

structured_output_agent = Agent(
    model=model.local,
    description="You write movie scripts.",
    response_model=MovieScript,
)

q = "Shanghai"

structured_output_agent.print_response(q, stream=True)

# more details
response: RunResponse = structured_output_agent.run(q)
pprint(type(response.content)) # -> <class '__main__.MovieScript'>
pprint(response.content)
