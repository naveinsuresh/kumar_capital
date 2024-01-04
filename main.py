import openai
import gradio
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get("KEY")

# GPT Prompt
message_chain = [
    {
        "role": "system",
        "content": """You are the voice of Kumar Capital, a leading financial consulting agency.
        Your mission is to provide expert guidance on finance, investing, and capital markets.
        Stay focused on these topics, avoiding unrelated discussions.
        Cultivate a friendly, caring, and creative tone in your responses to better assist and engage clients.""",
    }
]


# Main
def CustomChatGPT(input):
    message_chain.append({"role": "user", "content": input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message_chain
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    message_chain.append({"role": "assistant", "content": ChatGPT_reply})
    print(input)
    return ChatGPT_reply


# Front End Chat Interface
demo = gradio.Interface(
    fn=CustomChatGPT, inputs="text", outputs="text", title="Kumar Capital"
)


# Launch
demo.launch(share=True)


# Disclaimer
### This project is made with the understanding that neither the AI Bot nor the developer is engaged in rendering legal, accounting, or other professional advice. Since the details of your situation are fact-dependent, you should additionally seek the services of a competent professional. ###
