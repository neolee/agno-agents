from agno.embedder.ollama import OllamaEmbedder
from agno.embedder.openai import OpenAIEmbedder
from mal.providers import Provider, provider_by_alias


def test_embedder(s, embedder):
    embeddings = embedder.get_embedding(s)
    print(f"Embeddings: {embeddings[:5]}")
    print(f"Dimensions: {len(embeddings)}")

def test_ollama_embedder(s: str, model_id: str, dimensions: int):
    embedder = OllamaEmbedder(id=model_id, dimensions=dimensions)
    test_embedder(s, embedder)

def test_openai_compatible_embedder(s: str, provider: Provider, model_id: str, dimensions: int):
    embedder = OpenAIEmbedder(
        base_url=provider.base_url,
        api_key=provider.api_key,
        id=model_id,
        dimensions=dimensions
    )
    test_embedder(s, embedder)


# s = "The quick brown fox jumps over the lazy dog."
s = "路漫漫其修远兮，吾将上下而求索"

test_ollama_embedder(s, model_id="nomic-embed-text", dimensions=768)
local = provider_by_alias("local")
test_openai_compatible_embedder(s, local, model_id="snowflake", dimensions=1024)
qwen = provider_by_alias("qwen")
test_openai_compatible_embedder(s, qwen, model_id="text-embedding-v3", dimensions=1024)
