from azure.ai.evaluation import QAEvaluator
from openai_helper import AZURE_DEPLOYMENT,AZURE_OPENAI_API_KEY,AZURE_OPEN_API_VERSION,AZURE_OPENAI_ENDPOINT

# Initialize Azure OpenAI Connection with your environment variables
model_config = {
    "azure_endpoint": AZURE_OPENAI_ENDPOINT,
    "api_key": AZURE_OPENAI_API_KEY,
    "azure_deployment": AZURE_DEPLOYMENT,
    "api_version": AZURE_OPEN_API_VERSION,
}

# Initializing QA (question-answer) Evaluator with project information
qa_eval = QAEvaluator(model_config=model_config)
# Running QA Evaluator on single input row
qa_score = qa_eval(query="What is the capital of France?", response="Problably Paris.", context="Every country has a capital.", ground_truth="Paris is the capital of France.")
print(qa_score)
