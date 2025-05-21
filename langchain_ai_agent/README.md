# Langchain AI Agent

This is a basic Python project for an AI agent using the Langchain framework.

## Description

This project provides a starting template for building AI agents with Langchain. It includes a simple example of using an LLM (Large Language Model) chain to generate text based on a prompt.

## Setup

1.  **Clone the repository (if applicable):**
    ```bash
    # git clone <repository_url>
    # cd langchain_ai_agent
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Make sure you are in the `langchain_ai_agent` directory where `requirements.txt` is located.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set your OpenAI API Key:**
    This agent uses OpenAI's models. You need to set your OpenAI API key as an environment variable.
    ```bash
    export OPENAI_API_KEY='your_api_key_here'
    ```
    Replace `'your_api_key_here'` with your actual OpenAI API key.
    **Important:** Do not commit your API key directly into the code if you are using version control.

## Usage

Once the setup is complete, you can run the example agent:

1.  **Navigate to the project directory:**
    ```bash
    # cd langchain_ai_agent # If not already there
    ```

2.  **Run the agent script:**
    ```bash
    python agent.py
    ```

    The script will execute the example Langchain chain and print the output from the AI model.

## Customization

You can modify `agent.py` to:
*   Change the LLM model.
*   Define different prompt templates.
*   Create more complex chains or agents.
*   Integrate other Langchain components like memory, tools, etc.

## Running with Docker

To build and run this application using Docker, follow these steps:

1.  **Build the Docker image:**
    Navigate to the `langchain_ai_agent` directory in your terminal and run:
    ```bash
    docker build -t langchain-agent .
    ```

2.  **Run the Docker container:**
    You need to pass your OpenAI API key as an environment variable to the container.
    Replace `your_api_key_here` with your actual OpenAI API key.
    ```bash
    docker run -e OPENAI_API_KEY='your_api_key_here' langchain-agent
    ```

    The application will then run inside the Docker container, and you should see the output in your terminal.
