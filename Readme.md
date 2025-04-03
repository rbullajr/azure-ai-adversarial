# Exemplos de Simuladores da Azure AI

Esse repositório contém códigos de exemplo de uso dos simuladores da Azure AI, tanto para geração de conversas e ataques como para avaliações.

## Simulação de conversa, ataque e adversarial

Há uma documentação acerca de simulações de conversa, ataque e adversarial no link [Generate synthetic and simulated data for evaluation](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/simulator-interaction-data).
Contudo, a documentação é muito focada em um ambiente que já está pronto para desenvolvimento.

Nesse sentido, o respositório corrente apresenta exemplos completos de uso das simulações, bem como uma preparação do ambiente.

### Preparação do ambiente (Azure)

Para que a biblioteca consiga se conectar ao ambiente da Azure para a geração das simulações, é necessário instalar um software na máquina que gerencia e aplica as credenciais de usuário da Azure.

Há duas opções de CLI:

1. **Azure CLI** (recomendado)
    
    Instalável a partir do link: [How to install the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
  
    Após, realizar login por meio das instruções [Authenticate to Azure using Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli)

    Há ainda nesse projeto um arquivo com exemplos de alguns comandos: [``comandos-azure-cli.md``](comandos-azure-cli.md)

2. **Azure Developer CLI**

    Instalável a partir do link: [instalação Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd?tabs=winget-windows%2Cbrew-mac%2Cscript-linux&pivots=os-windows)

    Após, realizar login por meio do comando ``azd auth login``, detalhes em [Azure Developer CLI reference](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference#azd-auth-login)
  


Nos códigos de exemplos deste repositório, foi utilizada a opção (**Azure CLI**).
Mas se a outra opção for a selecionada, será necessário alterar a classe (objeto) no código que referencia a credencial.
Ou seja, será necessário alterar a credencial de ``AzureCliCredential`` para ``AzureDeveloperCliCredential`` nos códigos.


### Preparação

#### Python

O código foi desenvolvido utilizando python versão 3.10.12

Antes de executar, não esquecer de instalar os pacotes indicados em ``requirements.txt``.
Recomenda-se o uso de [virtual environments](https://docs.python.org/3/library/venv.html) (``venv``).

#### Variáveis

É necessário configurar o arquivo ``.env`` com as variáveis de ambiente.

Configurar os dados de projeto de modo a refletir os dados da conta da Azure utilizada:
```
SUBSCRIPTION_ID=
RESOURCE_GROUP_NAME=
PROJECT_NAME=
```


Configurar o modelo para a geração da simulação (será usado em todos as simulações):

```
AZURE_OPENAI_ENDPOINT=https://teste-adversarial.openai.azure.com
AZURE_OPENAI_API_KEY=<chave de acesso>
AZURE_DEPLOYMENT=gpt-4o-mini
AZURE_OPEN_API_VERSION=2023-03-15-preview
```

Configurar o alvo a ser experimentado (somente usado na Simualção Simples):

- Exemplo caso seja Open AI:
    ```
    TARGET_TYPE=openai
    TARGET_OPENAI_API_KEY=<chave de acesso>
    TARGET_OPENAI_MODEL=gpt-4o-mini
    ```

- Exemplo caso seja Azure AI:
    ```
    TARGET_TYPE=azure
    TARGET_OPENAI_ENDPOINT=https://teste-adversarial.openai.azure.com
    TARGET_OPENAI_API_KEY=<chave de acesso>
    TARGET_OPENAI_MODEL=gpt-4o-mini
    TARGET_OPENAI_API_VERSION=2023-03-15-preview
    ```


### Códigos de exemplos

Há quatro códigos de exemplos de cada um dos tipos de simulação:

- Simulação simples: código [``simulation.py``](./simulation.py);

- Simulação Adversarial: código [``adversarial_simulation.py``](./adversarial_simulation.py);

- Simulação de Ataque Direto: código [``direct_attack_simulation.py``](./direct_attack_simulation.py);

- Simulação de Ataque Indireto: código [``indirect_attack_simulation.py``](./indirect_attack_simulation.py).


## Exemplos de Avaliações (Evaluation)

Os exemplos aqui demonstrados são extraídos do documento [Evaluate with the Azure AI Evaluation SDK](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/evaluate-sdk)

### Preparação

Utilizar as mesmas preparações realizadas na secão [Preparação](#preparação).

### Códigos de exemplos

Há três códigos de exemplos:

- Avaliação de de relevância: [``relevance_evaluator.py``](./relevance_evaluator.py);

- Avaliação de violência: [``violence_evaluator.py``](./violence_evaluator.py);

- Avaliação composite de QA: [``composite_qa_evaluator.py``](./composite_qa_evaluator.py).