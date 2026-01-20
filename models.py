from agno.models.deepseek.deepseek import DeepSeek

from mal.providers import deepseek_provider
from mal.adapter.agno import model


deepseek = DeepSeek(id=deepseek_provider.model_id)
deepseek_reasoner = DeepSeek(id=deepseek_provider.reasoner_model_id)

qwen = model("qwen/qwen-plus-latest")
qwen_coder = model("qwen/qwen3-coder-plus")

openrouter_gemini_flash = model("openrouter/google/gemini-3-flash-preview")
openrouter_gemini_pro = model("openrouter/google/gemini-3-pro-preview")

local = model("local")

default = qwen
default_reasoner = deepseek_reasoner
