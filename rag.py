from agno.agent.agent import Agent
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb.lance_db import LanceDb
from agno.vectordb.search import SearchType

import mal.agno.model as model


vector_db=LanceDb(
    table_name="articles",
    uri="db/lancedb",
    search_type=SearchType.vector,
    embedder=OllamaEmbedder(id="snowflake-arctic-embed2", dimensions=1024),
)

knowledge_base = PDFKnowledgeBase(
    path="db/pdfs",
    vector_db=vector_db
)

# BUG parameters not work, always recreate
# these 2 parameters are set their default values, keep them here just for note
knowledge_base.load(recreate=False, skip_existing=True)

agent = Agent(
    model=model.default,
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
)

# q = "What is the 'CAP Theorem' in software architecture?"
# q = "Explain to me what 'Illiberal Democracy' is"
q = "为什么我们要批判新制度经济学？"

agent.print_response(q, stream=True)
