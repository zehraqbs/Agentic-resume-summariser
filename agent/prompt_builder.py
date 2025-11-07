# app/agent/prompt_builder.py
from typing import Tuple, Protocol, Any

class ITaskPromptBuilder(Protocol):
    def to_prompt(self, input_data: Any, stream: bool = False) -> Tuple[str, str]:
        ...

class ResumeSummarizationPromptBuilder:
    """
    Builds prompts for summarizing resume data.
    """

    def to_prompt(self, resume_text: str, stream: bool = False) -> Tuple[str, str]:
        system_prompt = "You are a deterministic resume parser. You output EXACTLY 4 to 6 bullet points. NOTHING else ever. No intro. No JSON. No markdown. Every line starts with • followed by ONE space. You never split a bullet."
        user_prompt = f"""Resume:
{resume_text}

FOLLOW THIS OUTPUT FORMAT EXACTLY — REPLACE ONLY THE CONTENT:

• [Most recent job title] at [Company] ([Start]–Present)
• [X]+ years of experience at [Company1], [Company2] (if any)
• [Skill1], [Skill2], [Skill3], [Skill4], [Skill5], [Skill6], [Skill7], [Skill8], [Skill9], [Skill10], [Skill11], [Skill12]
• [Highest degree] [Major], [University] ([Years]), [GPA if listed]
• [Cert1] ([Year]), [Cert2] ([Year])   (only if "CERTIFICATIONS" section exists)
• [One strongest achievement]   (only if no certs and very impressive metric)

CRITICAL RULES YOU CANNOT BREAK:
- NEVER write more than 6 lines
- NEVER write less than 4 lines
- NEVER split any bullet across two lines
- NEVER cut off a skill like "Scikit,"
- NEVER hallucinate skills, years, or companies
- Fix typos: SageMaker → AWS SageMaker, Kubernets → Kubernetes, NodeJS → Node.js
- If no certifications → max 5 bullets
- If resume is short → combine education + degree in one bullet

You are a robot. You only fill the template. No creativity.

Output only the bullets. Start now:

• """

        return system_prompt, user_prompt
