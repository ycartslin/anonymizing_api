import requests

class LLMClient:
    def __init__(self, api_key, base_url="https://api.openai.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def query(self, model, prompt, max_tokens=150):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens
        }
        response = requests.post(f"{self.base_url}/completions", headers=headers, json=data)
        return response.json()
