import os
from langchain_openai import ChatOpenAI


#using os.environ
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", None)
OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME", "gpt-3.5-turbo")

if not OPENAI_API_KEY:
    raise NotImplementedError("`OPENAI_API_KEY` environment variable is not set")


def get_openai_llm():
    openai_parameters = {
        "model": OPENAI_MODEL_NAME,
        "api_key": OPENAI_API_KEY
    }
    if OPENAI_BASE_URL:
        openai_parameters["base_url"] = OPENAI_BASE_URL

    
    return ChatOpenAI(**openai_parameters)

