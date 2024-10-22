import os
from typing import Dict
from dotenv import load_dotenv
from openai import AzureOpenAI,OpenAI


load_dotenv()

AZURE_OPENAI_ENDPOINT=os.getenv('AZURE_OPENAI_ENDPOINT')
AZURE_OPENAI_API_KEY=os.getenv('AZURE_OPENAI_API_KEY')
AZURE_DEPLOYMENT=os.getenv('AZURE_DEPLOYMENT')
AZURE_OPEN_API_VERSION=os.getenv('AZURE_OPEN_API_VERSION')


TARGET_TYPE = os.getenv('TARGET_TYPE')
TARGET_OPENAI_API_KEY = os.getenv('TARGET_OPENAI_API_KEY')
TARGET_OPENAI_ENDPOINT = os.getenv('TARGET_OPENAI_ENDPOINT')
TARGET_OPENAI_API_VERSION = os.getenv('TARGET_OPENAI_API_VERSION')
TARGET_OPENAI_MODEL = os.getenv('TARGET_OPENAI_MODEL')

if TARGET_TYPE == 'azure':
        client = AzureOpenAI(
                        azure_endpoint=TARGET_OPENAI_ENDPOINT,
                        api_version=TARGET_OPENAI_API_VERSION,
                        api_key=TARGET_OPENAI_API_KEY,
                )
elif TARGET_TYPE == 'openai':
        client = OpenAI(base_url=TARGET_OPENAI_ENDPOINT, api_key=TARGET_OPENAI_API_KEY)


azure_ai_project:Dict = {
    "subscription_id": os.getenv('SUBSCRIPTION_ID'),
    "resource_group_name": os.getenv('RESOURCE_GROUP_NAME'),
    "project_name": os.getenv('PROJECT_NAME')
}
