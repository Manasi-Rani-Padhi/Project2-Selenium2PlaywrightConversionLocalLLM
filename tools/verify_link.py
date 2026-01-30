import requests
import json

def verify_ollama(model="qwen2:0.5b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": "Say 'Ollama is linked' if you can read this.",
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        print(f"Response from {model}: {result.get('response', '').strip()}")
        return True
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")
        return False

if __name__ == "__main__":
    # Test with qwen2 as it's lighter
    if verify_ollama("qwen2:0.5b"):
        print("Link Phase: SUCCESS")
    else:
        print("Link Phase: FAILED")
