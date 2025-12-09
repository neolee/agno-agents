from agno.models.ollama.chat import Ollama
from agno.models.deepseek.deepseek import DeepSeek

from mal.providers import deepseek_provider, ollama_provider
from mal.adapter.agno import model


deepseek = DeepSeek(id=deepseek_provider.model_id)
deepseek_reasoner = DeepSeek(id=deepseek_provider.reasoner_model_id)

qwen = model("qwen/qwen-plus-latest")
qwen_coder = model("qwen/qwen3-coder-plus")

openrouter_gemini_flash = model("openrouter/google/gemini-2.5-flash")
openrouter_gemini_pro = model("openrouter/google/gemini-3-pro-preview")

local = model("local")

lmstudio = model("lmstudio")

ollama = Ollama(ollama_provider.model_id)

default = qwen
default_reasoner = deepseek_reasoner
