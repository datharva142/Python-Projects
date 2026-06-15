import requests
import json

def ask_llm(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Please ensure Ollama is running locally with the Llama3 model."
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"
