from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.vectordb.lancedb.lance_db import LanceDb
from agno.vectordb.search import SearchType

from embedders import snowflake
from util.fs import list_files_as_strs
import models as m


vector_db=LanceDb(
    table_name="articles",
    uri="db/lancedb",
    search_type=SearchType.vector,
    embedder=snowflake,
)

knowledge = Knowledge(
    vector_db=vector_db
)

parent = "./db/pdfs"
paths = list_files_as_strs(parent, ".pdf")
for path in paths:
    knowledge.add_content(
        path=path,
        reader=PDFReader(),
    )

agent = Agent(
    model=m.default,
    knowledge=knowledge,
    markdown=True,
)

# q = "What is the 'CAP Theorem' in software architecture?"
# q = "Explain to me what 'Illiberal Democracy' is"
q = "为什么我们要批判新制度经济学？"

agent.print_response(q, stream=True)
