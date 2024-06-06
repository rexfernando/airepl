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

Run the script with the required `--token` argument and optional `--url` and `--model` arguments:

```sh
airepl.py [-h] [--url URL] --token TOKEN [--model MODEL]

