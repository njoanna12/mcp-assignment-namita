# my_question.py
# Asks the MCP server one question and prints its answer.
import asyncio
import json

from agents.mcp import MCPServerStdio
from mcp_client_demo import params, call   # reuse the demo's connection settings

QUESTION = "What is the accuracy of each model?"


async def main():
    async with MCPServerStdio(params=params, client_session_timeout_seconds=120) as server:
        result = await call(server, "confusion_matrix_metrics", {"request_id": "my-question"})

        print("Question:", QUESTION)
        print("Tool used: confusion_matrix_metrics")
        print()
        for model in ["logistic_regression", "knn"]:
            print(f"{model}: accuracy = {result[model]['accuracy']:.1%}")
        print()
        print("Full response from the MCP server:")
        print(json.dumps(result, indent=2))


asyncio.run(main())