from typing import List

from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import END, MessageGraph
from chains import first_responder, revisor
from tool_executor import tool_node



res = graph.invoke(
    "Write about AI-Powered SOC / autonomous soc  problem domain, list startups that do that and raised capital."
)

print(res[-1].tool_calls[0]["args"]["answer"])
print(res)
