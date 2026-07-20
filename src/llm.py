from abc import ABC, abstractmethod

from ollama import Client
from openai import OpenAI

from src.config import (
    LLM_PROVIDER,
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)


class BaseLLM(ABC):
    """
    Base interface for all LLM providers.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate text from the supplied prompt.
        """
        raise NotImplementedError


# ============================================================
# OpenAI
# ============================================================

class OpenAIService(BaseLLM):
    """
    OpenAI implementation.
    """

    def __init__(self) -> None:

        if not OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not configured."
            )

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        try:

            response = self.client.responses.create(
                model=OPENAI_MODEL,
                input=prompt,
            )

            return response.output_text.strip()

        except Exception as error:

            raise RuntimeError(
                f"OpenAI Error: {error}"
            ) from error


# ============================================================
# Ollama
# ============================================================

class OllamaService(BaseLLM):
    """
    Ollama implementation.
    """

    def __init__(self) -> None:

        self.client = Client(
            host=OLLAMA_BASE_URL
        )

    def generate(self, prompt: str) -> str:

        try:

            response = self.client.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            return response["message"]["content"].strip()

        except Exception as error:

            raise RuntimeError(
                f"Ollama Error: {error}"
            ) from error


# ============================================================
# Factory
# ============================================================

def get_llm() -> BaseLLM:
    """
    Return the configured LLM provider.
    """

    provider = LLM_PROVIDER.lower()

    if provider == "openai":
        return OpenAIService()

    if provider == "ollama":
        return OllamaService()

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )