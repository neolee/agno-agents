from agno.embedder.ollama import OllamaEmbedder
from agno.embedder.openai import OpenAIEmbedder
from mal.providers import Provider, local_provider, qwen_provider


def openai_embedder(provider: Provider, model_id: str, dimensions: int) -> OpenAIEmbedder:
    embedder = OpenAIEmbedder(
        base_url=provider.base_url,
        api_key=provider.api_key,
        id=model_id,
        dimensions=dimensions
    )
    return embedder

def ollama_embedder(model_id: str, dimensions: int) -> OllamaEmbedder:
    embedder = OllamaEmbedder(id=model_id, dimensions=dimensions)
    return embedder


nomic = openai_embedder(local_provider, "nomic", 768)
snowflake = openai_embedder(local_provider, "snowflake", 1024)
aliyun = openai_embedder(qwen_provider, "text-embedding-v3", 1024)


if __name__ == "__main__":
    def test_embedder(s, embedder):
        embeddings = embedder.get_embedding(s)
        print(f"Embeddings: {embeddings[:5]}")
        print(f"Dimensions: {len(embeddings)}")

    # s = "The quick brown fox jumps over the lazy dog."
    s = "路漫漫其修远兮，吾将上下而求索"

    # test_embedder(s, ollama_embedder("nomic-embed-text", 768))
    test_embedder(s, nomic)
    test_embedder(s, snowflake)
    test_embedder(s, aliyun)
