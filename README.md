# 🔍 RepoLens

**RepoLens** is an autonomous AI agent designed to scan, analyze, and document entire code repositories. Built for the 2026 Claude Code Hackathon, it transforms complex codebases into structured, living documentation using high-speed inference.

---

## 🚀 Key Features

- **LPU™ Powered Analysis**: Leverages Groq's Inference Engine for near-instant repository auditing.
- **Context-Aware Summarization**: Automatically reads project files and identifies core architectural patterns.
- **Living Documentation**: Generates a professional-grade documentation site that updates as your code evolves.
- **Production-Ready Layout**: Implements the `src/` directory standard for clean, modular development.

## 🛠️ Tech Stack

- **Inference Engine**: [Groq Cloud](https://console.groq.com/)
- **Model**: `llama-3.3-70b-versatile` (State-of-the-art 70B parameter model)
- **Programming Language**: Python 3.10+
- **Documentation Framework**: [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- **Diagramming**: Mermaid.js support via MkDocs plugins.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sandeep-dgn/repolens
   cd repolens

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

## 🔐 Configuration
RepoLens requires a Groq API key to function. Create a .env file in the root directory:
 ```plaintext
 GROQ_API_KEY=gsk_your_actual_key_here


## 📖 Usage

1. **Run the AI Analyst**
Execute the main script to scan your repository and generate a code summary:
 ```bash
 python main.py



   
  