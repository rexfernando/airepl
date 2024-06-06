import argparse
from openai import OpenAI

def parse_args():
    parser = argparse.ArgumentParser(description="OpenAI REPL Client")
    parser.add_argument('--url', type=str, help='The OpenAI API URL (default: https://api.openai.com/v1/chat/completions)')
    parser.add_argument('--token', type=str, required=True, help='The OpenAI API Token')
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo', help='The model to use (default: gpt-3.5-turbo)')
    parser.add_argument('--stream', type=bool, default=True, help='Stream the response (default: True)')
    parser.add_argument('--temp', type=float, default=0.01, help='The temperature to use for the completions (default: 0.01)')
    return parser.parse_args()

def main():
    args = parse_args()
    url = args.url if args.url else "https://api.openai.com/v1/chat/completions"
    client = OpenAI(api_key=args.token, base_url=url)

    print(f"Connected to OpenAI API at {url} using model {args.model}")

    stream = args.stream
    temperature = args.temp

    while True:
        try:
            prompt = input(">>> ")
            if prompt.lower() in ["exit", "quit"]:
                break

            response = client.chat.completions.create(
                model=args.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                stream=stream
            )

            if stream:
                response_text = ""
                print("Streamed response:")
                for chunk in response:
                    print(chunk.choices[0].delta.content, end="")
                    response_text += chunk.choices[0].delta.content
                usage = chunk.usage
                finish_reason = chunk.choices[0].finish_reason
                print("\n")
            else:
                response_text = response.choices[0].message.content
                usage = response.usage
                finish_reason = response.choices[0].finish_reason
                print(response_text)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

