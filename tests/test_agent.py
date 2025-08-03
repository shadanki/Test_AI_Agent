import pytest
from agent.agent import Agent

def test_agent_quit(monkeypatch, capsys):
  inputs = iter(["quit"])
  monkeypatch.setattr('builtins.input', lambda _: next(inputs))

  agent = Agent(system_prompt="テスト")
  agent.run()

  captured = capsys.readouterr()
  assert "Goodbye!" in captured.out