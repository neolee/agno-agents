from agno.models.ollama.chat import Ollama
from agno.models.deepseek.deepseek import DeepSeek

import mal.providers as mal
from mal.agno.client import model_by_provider, model_by_provider_with_model


deepseek = DeepSeek(id=mal.deepseek_provider.model_id)
deepseek_reasoner = DeepSeek(id=mal.deepseek_provider.reasoner_model_id)

qwen = model_by_provider(mal.qwen_provider)
qwen_coder = model_by_provider(mal.qwen_provider, model_type="coder")
qwen_reasoner = model_by_provider(mal.qwen_provider, model_type="reasoner")

openrouter = model_by_provider(mal.openrouter_provider)
openrouter_gemini_flash = model_by_provider_with_model(mal.openrouter_provider, model_name="google/gemini-2.5-flash")
openrouter_gemini_pro = model_by_provider_with_model(mal.openrouter_provider, model_name="google/gemini-2.5-pro")

local = model_by_provider(mal.local_provider)

lmstudio = model_by_provider(mal.lmstudio_provider)

ollama = Ollama(mal.ollama_provider.model_id)

default = qwen
default_reasoner = deepseek_reasoner
