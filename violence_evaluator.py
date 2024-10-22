from azure.identity import AzureCliCredential
from azure.ai.evaluation import ViolenceEvaluator
from openai_helper import azure_ai_project

# Initializing Violence Evaluator with project information
violence_eval = ViolenceEvaluator(azure_ai_project, credential=AzureCliCredential())
# Running Violence Evaluator on single input row
violence_score = violence_eval(query="What is the capital of France?", response="Paris.")
print(violence_score)
