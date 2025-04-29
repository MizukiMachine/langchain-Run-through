import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_community.llms import OpenAI as LangChainOpenAI  # ← LangChain用（別名）
from langchain_community.chat_models import ChatOpenAI


# 環境変数ロード
load_dotenv(find_dotenv())

# OpenAIクライアント作成
client = OpenAI()

# モデル名
llm_model = "gpt-3.5-turbo"


# ChatOpenAIラッパー（LangChain用）
chat_model = ChatOpenAI(temperature=0.7)

# APIにリクエストする関数
def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

customer_review = """
    あなたたちの製品はひどいです。
    どうやってこんなものを市場に出せたのか理解できません。
    私はこんなもの欲しくありませんし、正直誰も欲しがるべきではありません。
    今すぐお金を返してください。
"""

tone = """きちんとした日本語で、親しみやすく温かみがあり、敬意を込めた口調。
"""
language = "English"

promp = f"""
    以下の {customer_review} を {tone} で書き直し、
    その後、新しいレビュー分を {language} に翻訳してください。
"""

rewrite = get_completion(prompt=promp)
print(rewrite)
