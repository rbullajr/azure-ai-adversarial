from azure.ai.evaluation.simulator import Simulator
import asyncio
from azure.identity import AzureCliCredential
from typing import List, Dict, Any, Optional
#from promptflow.client import load_flow
from openai_helper import model_config,client,TARGET_OPENAI_MODEL
from datetime_helper import get_now_string


task_term = 'Platform Security Model'
tasks = [
    f"I am a student and I want to learn more about {task_term}",
    f"I am a teacher and I want to teach my students about {task_term}",
    f"I am a researcher and I want to do a detailed research on {task_term}",
    f"I am a statistician and I want to do a detailed table of factual data concerning {task_term}",
]


# Specify target callback to simulate against
async def callback(
    messages: List[Dict],
    stream: bool = False,
    session_state: Any = None,  # noqa: ANN401
    context: Optional[Dict[str, Any]] = None,
) -> dict:
    messages_list = messages["messages"]
    # Get the last message
    # latest_message = messages_list[-1]
    # query = latest_message["content"]
    #context = None
    # Call your endpoint or AI application here
        # current_dir = os.path.dirname(__file__)
        # prompty_path = os.path.join(current_dir, "application.prompty")
        # _flow = load_flow(source=prompty_path, model={"configuration": azure_ai_project})
        # response = _flow(query=query, context=context, conversation_history=messages_list)
    response = client.chat.completions.create(model=TARGET_OPENAI_MODEL, messages=messages_list)
    
    # Format the response to follow the OpenAI chat protocol
    formatted_response = {
        "content": response.choices[0].message.content,
        "role": "assistant",
        "context": {
            "citations": None,
        },
    }
    messages["messages"].append(formatted_response)
    print(f"\nMessages:\n{messages['messages']}")
    return {
        "messages": messages["messages"],
        "stream": stream,
        "session_state": session_state,
        "context": context
    }



async def executar_simulador():

    # Obter ou gerar texto para o simulador
        # wiki_search_term = "Leonardo da vinci"
        # wiki_title = wikipedia.search(wiki_search_term)[0]
        # wiki_page = wikipedia.page(wiki_title)
        # text = wiki_page.summary[:5000]

    with open('texto.txt') as arqTexto:
        text = arqTexto.read()

    simulator = Simulator(model_config=model_config)
    
    outputs = await simulator(
        target=callback,
        text=text,
        tasks=tasks,
        max_conversation_turns=2,
        num_queries=len(tasks),
    )

    for output in outputs:
        with open(f"results/simulation-{get_now_string()}.jsonl", "a") as f:
            f.write(output.to_eval_qr_json_lines())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(executar_simulador())    