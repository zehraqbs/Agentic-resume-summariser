# app/agent/agent_utility.py
import asyncio
from typing import Any, AsyncGenerator, Optional, List, TypeVar, Generic
from inference.inference_utility import InferenceUtility
from agent.prompt_builder import ITaskPromptBuilder
from agent.output_mapper import IOutputMapper

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")

class AgentUtility(Generic[TInput, TOutput]):
    """
    Python equivalent of GroqAgentUtility.cs
    Orchestrates prompt -> inference -> output mapping
    """

    def __init__(self, inference_service: Optional[InferenceUtility] = None):
        self._inference_service = inference_service or InferenceUtility()

    async def run_task_async(
        self,
        input_data: TInput,
        prompt_builder: ITaskPromptBuilder,
        output_mapper: IOutputMapper,
        extra_stop_words: Optional[List[str]] = None,
        throw_on_stop_word: bool = False
    ) -> TOutput:
        """
        Runs a single LLM task end-to-end (non-streaming)
        """
        system_prompt, user_prompt = prompt_builder.to_prompt(input_data, stream=False)
        response = await self._inference_service.get_chat_completion(
            system_prompt,
            user_prompt,
            extra_stop_words=extra_stop_words,
            throw_on_stop_word=throw_on_stop_word
        )
        return output_mapper.to_output(response)

    async def stream_task_async(
        self,
        input_data: TInput,
        prompt_builder: ITaskPromptBuilder,
        output_mapper: IOutputMapper
    ) -> AsyncGenerator[TOutput, None]:
        """
        Streams response chunks as they come from the LLM
        """
        system_prompt, user_prompt = prompt_builder.to_prompt(input_data, stream=True)

        async for chunk in self._inference_service.stream_chat_completion(
            system_prompt, user_prompt
        ):
            yield output_mapper.to_output(chunk or "")
