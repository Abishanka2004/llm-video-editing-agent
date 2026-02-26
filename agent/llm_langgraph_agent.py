import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import TypedDict, List

from langgraph.graph import StateGraph, END

#from langchain_community.chat_models import ChatOllama
from langchain_groq import ChatGroq

# your tools
from agent.executor import execute


# Load LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)


# Agent state
class AgentState(TypedDict):

    input_video: str
    instruction: str
    tasks: List[str]
    output: str


import json

def llm_node(state):

    prompt = f"""
You are a strict video editing agent.

Allowed tasks:
- extract_audio
- generate_subtitles
- trim
- remove_silence

User instruction:
{state["instruction"]}

Rules:
1. Return ONLY a JSON array.
2. Do NOT explain.
3. Do NOT add extra text.
4. Only include tasks explicitly required.
5. If unsure, return [].

Example:
["generate_subtitles"]
"""

    response = llm.invoke(prompt)

    raw = response.content.strip()

    print("Raw LLM output:", raw)

    try:
        tasks = json.loads(raw)
    except:
        tasks = []

    # 🔒 Safety filter — only allow valid tasks
    allowed = {"extract_audio", "generate_subtitles", "trim", "remove_silence"}
    tasks = [t for t in tasks if t in allowed]

    print("Final validated tasks:", tasks)

    return {"tasks": tasks}



# Executor node
def executor_node(state):
    print("Executor received tasks:", state["tasks"])

    output = execute(state["tasks"], state["input_video"])

    return {"output": output}


# Build graph
def create_agent():

    graph = StateGraph(AgentState)

    graph.add_node("llm", llm_node)

    graph.add_node("executor", executor_node)

    graph.set_entry_point("llm")

    graph.add_edge("llm", "executor")

    graph.add_edge("executor", END)

    return graph.compile()
