from dotenv import load_dotenv
from openai_helper import client,TARGET_OPENAI_MODEL,TARGET_OPENAI_ENDPOINT,TARGET_OPENAI_API_KEY,TARGET_OPENAI_API_VERSION,TARGET_TYPE

load_dotenv()


def chamar_openapi_teste():
    print(f'Variáveis para {TARGET_TYPE}: {TARGET_OPENAI_MODEL} {TARGET_OPENAI_API_VERSION} {TARGET_OPENAI_ENDPOINT} {TARGET_OPENAI_API_KEY} ')
    response = client.chat.completions.create(
        model=TARGET_OPENAI_MODEL,
        messages=[
            {
                "role": "user",
                "content": "Say hi!",
            }
        ]

    )
    print(response.choices[0].message.content)


if __name__ == '__main__':
    chamar_openapi_teste()
    
