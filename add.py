import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain_community.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"

prompt = "宇宙の年齢は何歳ですか？"
messages = [HumanMessage(content=prompt)]
llm = OpenAI(temperature=0.7)
chat_model = ChatOpenAI(temperature=0.7)

print(llm.predict("京都の天気は?"))
print("===================")
print(chat_model.predict_messages(messages).content)
# print(chat_model.predict("京都の天気は?"))