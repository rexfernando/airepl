
# OpenAI REPL Client

This is a simple REPL (Read-Eval-Print Loop) client for interacting with the OpenAI API using Python. The client connects to the OpenAI API, sends user prompts, and prints the responses.

## Prerequisites

- Python 3.6 or higher
- An OpenAI API key

## Installation

1. Clone this repository or download the script.

2. Install the required Python packages using pip:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script with the required `--token` argument and optional `--url`, `--model`, `--stream`, and `--temperature` arguments:

```sh
python airepl.py --token YOUR_API_TOKEN [--url URL] [--model MODEL] [--stream STREAM] [--temperature TEMPERATURE]
```

### Arguments:

- `--url`: The OpenAI API URL (default: https://api.openai.com/v1/chat/completions)
- `--token`: The OpenAI API Token (required)
- `--model`: The model to use (default: gpt-3.5-turbo)
- `--stream`: Stream the response (default: True)
- `--temp`: The temperature to use for the completions (default: 0.01)

### Example:

```sh
python airepl.py --token YOUR_API_TOKEN --model gpt-3.5-turbo --stream True --temperature 0.7
```

## Exit the REPL

To exit the REPL, type `exit` or `quit` and press Enter.

## Error Handling

If an error occurs, the script will print the error message.

