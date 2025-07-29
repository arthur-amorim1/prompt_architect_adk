"""Prompt Architect: build prompts for LLMs"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt

MODEL = "gemini-2.5-pro"

prompt_architect_agent = LlmAgent(
    name="prompt_architect",
    model=MODEL,
    description="Um assistente especialista que ajuda os usuários a construir prompts eficazes por meio de um diálogo guiado.",
    instruction=prompt.PROMPT_ARCHITECT_SYSTEM_PROMPT,
    tools=[],
)

root_agent = prompt_architect_agent
