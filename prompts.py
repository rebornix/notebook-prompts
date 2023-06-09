import base64
import os
import re
import openai
from IPython.display import Markdown, display

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_first_markdown_code_block(string):
    """
    This function takes a string as input and returns the first markdown code block found in the string.
    """
    pattern = re.compile(r"```[\s\S]*?```")
    match = pattern.search(string)
    if match:
        return match.group(0)
    else:
        return None


def display_codeblock(output):
    """
    This function takes a string as input, parse the first code block and displays it as a markdown codeblock.
    """
    display(Markdown(get_first_markdown_code_block(output)))

def get_system_prompt():
    return """
"""

def chatbot_response(system_prompt, user_prompt):
    """
    This function takes a user prompt as input and returns the chatbot response.
    """
    messages = [{"role": "system", "content": system_prompt}]
    for prompt in user_prompt:
        messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        engine="Turbo",
        # model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )

    display(Markdown(response["choices"][0]["message"]["content"]))
    return response["choices"][0]["message"]["content"]

def generate_user_prompts_a():
    """
    This function takes the active cell content, the cells above and the cells below and generates a prompt for the user.
    """
    prompt = []
    prompt.append("Print Hello World")
    return prompt
