from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb.lance_db import LanceDb
from agno.vectordb.search import SearchType

from embedders import snowflake
import models as m


vector_db=LanceDb(
    table_name="articles",
    uri="db/lancedb",
    search_type=SearchType.vector,
    embedder=snowflake,
)

knowledge_base = PDFKnowledgeBase(
    path="db/pdfs",
    vector_db=vector_db
)

# BUG parameters not work, always recreate
# these 2 parameters are set their default values, keep them here just for note
knowledge_base.load(recreate=False, skip_existing=True)

agent = Agent(
    model=m.default,
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
)

# q = "What is the 'CAP Theorem' in software architecture?"
# q = "Explain to me what 'Illiberal Democracy' is"
q = "为什么我们要批判新制度经济学？"

agent.print_response(q, stream=True)
