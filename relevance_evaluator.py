from azure.ai.evaluation import RelevanceEvaluator
from openai_helper import AZURE_DEPLOYMENT,AZURE_OPENAI_API_KEY,AZURE_OPEN_API_VERSION,AZURE_OPENAI_ENDPOINT

# Initialize Azure OpenAI Connection with your environment variables
model_config = {
    "azure_endpoint": AZURE_OPENAI_ENDPOINT,
    "api_key": AZURE_OPENAI_API_KEY,
    "azure_deployment": AZURE_DEPLOYMENT,
    "api_version": AZURE_OPEN_API_VERSION,
}

# Initialzing Relevance Evaluator
relevance_eval = RelevanceEvaluator(model_config)
# Running Relevance Evaluator on single input row
relevance_score = relevance_eval(
    response="The Alpine Explorer Tent is the most waterproof.",
    context="From the our product list,"
    " the alpine explorer tent is the most waterproof."
    " The Adventure Dining Table has higher weight.",
    query="Which tent is the most waterproof?",
)
print(relevance_score)
