# Agents based on `agno`

## Setup

``` shell
# core
uv add agno openai ollama

# tools deps
uv add 'httpx[socks]' duckduckgo-search yfinance
uv add googlesearch-python pycountry
uv add crawl4ai

# rag deps
uv add lancedb tantivy pypdf sqlalchemy
```
