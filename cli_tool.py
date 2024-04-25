import argparse
from api_client import LLMClient

def main():
    parser = argparse.ArgumentParser(description="Interact with a large language model.")
    parser.add_argument("--api-key", required=True, help="API key for accessing the LLM")
    parser.add_argument("--model", default="text-davinci-003", help="Model ID")
    parser.add_argument("--prompt", required=True, help="Prompt for the model")
    args = parser.parse_args()

    client = LLMClient(api_key=args.api_key)
    response = client.query(model=args.model, prompt=args.prompt)
    print(response['choices'][0]['text'])

if __name__ == "__main__":
    main()