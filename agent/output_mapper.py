# app/agent/output_mapper.py
from typing import Protocol, Any, Dict
import json
import re

class IOutputMapper(Protocol):
    def to_output(self, raw_response: str) -> Any:
        ...

class ResumeSummaryOutputMapper:
    """
    Converts the raw LLM text into a clean Python dict.
    """

    def to_output(self, raw_response: str) -> Dict[str, Any]:
        # Try to detect JSON if model returned it
        try:
            return json.loads(raw_response)
        except json.JSONDecodeError:
            pass

        # Otherwise clean text and return bullet points
        bullets = re.split(r"[\n•-]+", raw_response)
        bullets = [b.strip() for b in bullets if b.strip()]
        return {"summary_points": bullets}
