import re
from openai import OpenAI
from agent.prompt_templates import SYSTEM, USER

class Agent:
  def __init__(self, client: OpenAI, system_prompt: str):
    self.client = client
    self.history = [{"role": "system", "content": system_prompt}]

  def chat(self):
    resp = self.client.chat.completions.create(
      model="gpt-4o-mini",
      messages=self.history,
      temperature=0.7,
    )
    return resp.choices[0].message.content
  
  def run(self):
    while True:
      user_input = input("You: ")
      if user_input.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

      self.history.append({"role": "user", "content": USER.format(text=user_input)})
      result = self.chat()

      # ツール呼び出し検出
      if match := re.search(r"\[TOOL\] (\w+):(.+)", result):
        tool, arg = match.groups()
        from tools.stock_tool import fetch_stock_price
        if tool == "stock_price":
          price = fetch_stock_price(arg)
          self.history.append({"role": "tool", "content": f"{arg} price: {price}"})
          final = self.chat()
          print("Agent:", final)
        else:
          print("Agent", result)
      else:
        print("Agent:" , result)
      self.history.append({"role": "assistant", "content": result})