from mal.adapter.agno import openai_embedder



nomic = openai_embedder("local/nomic", 768)
snowflake = openai_embedder("local/snowflake", 1024)
aliyun = openai_embedder("qwen/text-embedding-v3", 1024)


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
