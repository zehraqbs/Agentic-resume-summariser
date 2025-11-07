# Agent_ai_candidate/inference/inference_utility.py
import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from typing import AsyncGenerator, Optional, List

# Load environment variables
load_dotenv()

class InferenceUtility:
    def __init__(self, model_name: str = "llama-3.1-8b-instant", temperature: float = 0.0):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

        self.llm = ChatGroq(
            groq_api_key=api_key,
            model=model_name,
            temperature=temperature,
            streaming=False
        )

    async def get_chat_completion(
        self,
        system_prompt: str,
        user_prompt: str,
        extra_stop_words: Optional[List[str]] = None,
        throw_on_stop_word: bool = False
    ) -> str:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        response = await self.llm.ainvoke(messages)
        text = response.content.strip()

        if extra_stop_words:
            for stop_word in extra_stop_words:
                if stop_word.lower() in text.lower():
                    if throw_on_stop_word:
                        raise ValueError(f"Guardrail triggered: {stop_word}")
                    text = text.replace(stop_word, "[REDACTED]")

        return text

    async def stream_chat_completion(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> AsyncGenerator[str, None]:
        stream_llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model=self.llm.model,
            streaming=True
        )

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

        async for chunk in stream_llm.astream(messages):
            yield chunk.content
