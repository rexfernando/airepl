import argparse
import openai

def parse_args():
    parser = argparse.ArgumentParser(description="OpenAI REPL Client")
    parser.add_argument('--url', type=str, help='The OpenAI API URL (default: https://api.openai.com/v1/chat/completions)')
    parser.add_argument('--token', type=str, required=True, help='The OpenAI API Token')
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo', help='The model to use (default: gpt-3.5-turbo)')
    return parser.parse_args()

def main():
    args = parse_args()

    openai.api_base = args.url if args.url else "https://api.openai.com/v1/chat/completions"
    openai.api_key = args.token

    print(f"Connected to OpenAI API at {openai.api_base} using model {args.model}")

    while True:
        try:
            prompt = input(">>> ")
            if prompt.lower() in ["exit", "quit"]:
                break

            response = openai.chat.completions.create(
                model=args.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            print(response.choices[0].message['content'].strip())
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

