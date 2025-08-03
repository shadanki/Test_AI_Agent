import os
from dotenv import load_dotenv
from openai import OpenAI
from agent.agent import Agent

def main():
  load_dotenv()

  api_key = os.getenv("OPENAI_API_KEY")
  if not api_key:
    raise RuntimeError("OPEN_API_KEY が設定されていません。環境変数か .env を確認してください。")
  
  client = OpenAI(api_key=api_key)
  agent = Agent(client=client, system_prompt="あなたは親切なアシスタントです。")
  agent.run() #ユーザー入力ループ開始

if __name__ == "__main__":
  main()