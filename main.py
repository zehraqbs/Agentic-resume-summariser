# main.py
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.agent_utility import AgentUtility
from agent.prompt_builder import ResumeSummarizationPromptBuilder
from agent.output_mapper import ResumeSummaryOutputMapper
from inference.inference_utility import InferenceUtility

# Create the FastAPI app
app = FastAPI(title="Agentic AI - Resume Summarizer API")

# Initialize our internal components
inference_service = InferenceUtility(model_name="llama-3.1-8b-instant")
agent = AgentUtility(inference_service)
prompt_builder = ResumeSummarizationPromptBuilder()
output_mapper = ResumeSummaryOutputMapper()

# Define request model
class ResumeRequest(BaseModel):
    text: str

# Define response model (optional for typing)
class ResumeSummary(BaseModel):
    summary_points: list[str]

@app.post("/summarize", response_model=ResumeSummary)
async def summarize_resume(request: ResumeRequest):
    """
    Summarize resume text using the Groq LLM.
    """
    try:
        result = await agent.run_task_async(
            request.text,
            prompt_builder,
            output_mapper
        )
        return {"summary_points": result.get("summary_points", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Agentic AI Resume Summarizer!"}

print("✅ FastAPI app loaded successfully")

# Run locally (only if executed directly)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
