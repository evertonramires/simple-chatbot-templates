# Simple Chatbot Templates

Simple Python scripts to chat with large language models (LLMs) from various sources. This README will guide you step by step—even if you’re new to Python or command-line tools.

[![Support my work ❤️](https://img.shields.io/badge/Support%20my%20work%20❤️-orange?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/c/orobocigano)



## Prerequisites
1. **Python 3.8+** installed.  
2. **pip** (Python package installer).  
3. **uv** cli tool (for virtual env & scripts).  
4. **ollama** installed if you plan to use the Ollama model backend.

## Installation

1. Clone the repository:
    ```
    git clone 
    cd chat-llm
    ```

2. Create and activate a virtual environment using `uv`:
    ```
    uv venv
    uv activate
    ```

3. Install Python dependencies:
    ```
    uv install -r requirements.txt
    ```

## Usage

All scripts use `uv run`. For example, to start a simple chat prompt with Ollama:

```
uv run prompt-chat-ollama.py
  
```
