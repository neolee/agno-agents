from agno.models.deepseek.deepseek import DeepSeek

from mal.providers import deepseek_provider
from mal.adapter.agno import model


deepseek = DeepSeek(id=deepseek_provider.model_id)
deepseek_reasoner = DeepSeek(id=deepseek_provider.reasoner_model_id)

qwen = model("qwen/qwen3.5-plus")

gpt = model("openai")

local = model("local")

default = qwen
default_reasoner = deepseek_reasoner
