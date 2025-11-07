# 🧠 Agentic AI Resume Summarizer

An **AI-powered resume summarization service** built using:
- 🦜 [LangChain](https://python.langchain.com/)
- ⚙️ [Groq API](https://console.groq.com/)
- ⚡ [FastAPI](https://fastapi.tiangolo.com/)
- 🔗 Optional [gRPC](https://grpc.io/) microservice layer

This project replicates the logic of a .NET agentic AI service — rewritten fully in Python — with a clean modular design and support for both HTTP and gRPC interfaces.

---

## 🚀 Features

✅ Summarizes long resumes into short, professional summaries  
✅ Built on top of **LangChain + Groq** for fast and accurate LLM inference  
✅ Modular structure for easy scaling and microservice integration  
✅ Includes **FastAPI** endpoint + optional **gRPC** server  
✅ Ready for **free deployment** on [Render](https://render.com/)

---

## 📁 Project Structure

Agentic_ai_candidate/
├── agent/
│ ├── agent_utility.py
│ ├── prompt_builder.py
│ ├── output_mapper.py
│ └── init.py
├── inference/
│ ├── inference_utility.py
│ ├── guardrail.py
│ ├── llm_client.py
│ ├── output_parser.py
│ └── init.py
├── proto/
│ └── resume.proto # gRPC schema
├── main.py # FastAPI entry point
├── grpc_server.py # Optional gRPC service
├── requirements.txt
├── render.yaml # Render deployment config
├── config.py
└── README.md


---
git clone https://github.com/<your-username>/Agentic_ai_candidate.git
cd Agentic_ai_candidate

2️⃣ Create and activate a virtual environment

python -m venv agentvenv
agentvenv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt
