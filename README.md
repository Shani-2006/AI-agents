# AI-agents
# AI Engineering & Automation Showcase 🚀

This repository demonstrates a collection of production-ready AI implementations, focusing on RAG architecture, structured data extraction, and autonomous agents.

## 🌟 Key Features & Modules

- **RAG (Retrieval-Augmented Generation):** Implementation of a knowledge-based system (`Rag.py`) using document embeddings to provide context-aware responses.
- **Structured Output & Data Integrity:** Leveraging **Pydantic** (`struct_whith_basemodel.py`) to ensure LLM outputs adhere to strict schemas, making them ready for API integration.
- **Agentic Capabilities:** Custom tool integration (`date_tool.py`) allowing the model to interact with external functions and real-time data.
- **Multimodal Processing:** Vision-based AI implementation (`llm_with_image.py`) for analyzing visual data.
- **Performance:** Optimized user experience using streaming responses (`chat_with_stream.py`).

## 🛠️ Technical Stack
- **Languages:** Python
- **AI Frameworks:** OpenAI SDK, LangChain (conceptual), Pydantic
- **Patterns:** Function Calling, System Prompt Engineering, RAG Pipeline

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt` (Note: ensure you have your `.env` file configured).
3. Run any module, e.g., `python Rag.py`.

---
*Developed as part of a professional technical assessment.*
