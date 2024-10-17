from azure.ai.evaluation.simulator import DirectAttackSimulator,AdversarialScenario
import asyncio
import json
from azure.identity import AzureCliCredential
from typing import List, Dict, Any, Optional
from promptflow.client import load_flow
from openai_helper import azure_ai_project


# Specify target callback to simulate against
async def callback(
    messages: List[Dict],
    stream: bool = False,
    session_state: Any = None
) -> dict:
    
    query = messages["messages"][0]["content"]
    context = None

    # Add file contents for summarization or re-write
    if 'file_content' in messages["template_parameters"]:
        query += messages["template_parameters"]['file_content']
    
    #messages_list = messages["messages"]
    #response = client.chat.completions.create(model=TARGET_OPENAI_MODEL, messages=messages_list)
    response = "RESPOSTA DUMMY"

    # Format the response to follow the OpenAI chat protocol
    formatted_response = {
        "content": response,#response.choices[0].message.content,
        "role": "assistant",
        "context": { }
    }
    messages["messages"].append(formatted_response)
    print(f"\nMessages:\n{messages['messages']}")
    return {
        "messages": messages["messages"],
        "stream": stream,
        "session_state": session_state
    }


async def executar_simulador():
    scenario = AdversarialScenario.ADVERSARIAL_QA
    simulator = DirectAttackSimulator(azure_ai_project=azure_ai_project, credential=AzureCliCredential())
    
    outputs = await simulator(
        scenario=scenario,
        target=callback,
        max_conversation_turns=2,
        max_simulation_results=10
    )

    with open("direct_attack_adversarial.jsonl", "a") as f:
        f.write(json.dumps(outputs))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(executar_simulador())
    