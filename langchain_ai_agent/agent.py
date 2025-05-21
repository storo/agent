import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# IMPORTANT: Set your OpenAI API key as an environment variable
# named OPENAI_API_KEY. For example, in your terminal:
# export OPENAI_API_KEY='your_api_key_here'
#
# Alternatively, you can uncomment the next line and add your key directly,
# but be careful not to commit your key to version control!
# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY" 

def main():
    # Check if the API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set your OpenAI API key to run this agent.")
        print("Example: export OPENAI_API_KEY='your_api_key_here'")
        return

    # Initialize the ChatOpenAI model
    # By default, it uses "gpt-3.5-turbo"
    llm = ChatOpenAI()

    # Define a prompt template
    prompt_template = ChatPromptTemplate.from_template(
        "You are a helpful assistant. What is a good name for a company that makes {product}?"
    )

    # Create an LLMChain
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # Example usage
    product_name = "colorful socks"
    print(f"Running chain with product: {product_name}")
    
    try:
        response = chain.invoke({"product": product_name})
        if isinstance(response, dict) and 'text' in response:
            print(f"Assistant's suggestion: {response['text']}")
        else:
            print(f"Received response: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your OpenAI API key is valid and has a current billing plan.")

if __name__ == "__main__":
    main()
