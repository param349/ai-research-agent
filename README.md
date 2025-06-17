# 🧠 AI Research Assistant

This project is a proof-of-concept (PoC) AI-powered Research Assistant built using Python and LangChain. It allows users to ask complex research queries and get structured, tool-augmented responses using an LLM (e.g., GPT-3.5 or local LLM via Ollama).

## 🚀 Features

- Natural language research queries
- Integrates with tools like:
  - Web Search
  - Wikipedia parsing
  - Local file creation & writing
- Supports both OpenAI GPT and local models (e.g., via Ollama)
- `.env` support for API key management

## 📁 Project Structure
.
├── main.py                # Entry point of the assistant
├── tools.py               # LLM and tool configurations
├── .env                   # Secret environment variables (not shared)
├── .gitignore             # Files/folders to ignore in version control
└── README.md              # Project documentation (this file)

🛠 Setup Instructions
1. Clone the repo
    git clone https://github.com/param349/ai-research-agent.git
    cd ai-research-agent

2. Create a virtual environment
    python -m venv ai_agent_venv
    ai_agent_venv\Scripts\activate  # For Windows

3. Install dependencies
    pip install -r requirements.txt

4. Add your .env file
    OPENAI_API_KEY=sk-...

5. Run the assistant
    python main.py

✅ Todo / Improvements
1. Add memory support for longer conversations
2. Integrate document upload for analysis
3. Add support for HuggingFace tools
4. Front-end interface (streamlit / flask / gradio)

🧑‍💻 Author
Parminder Singh
LinkedIn -https://www.linkedin.com/in/parminder349/

📜 License
This project is for educational and demonstration purposes only.
