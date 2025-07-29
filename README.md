# Prompt Architect Agent

Este projeto contém um agente desenvolvido com o Google Agent Development Kit (ADK).

## Descrição

O **Prompt Architect** é um agente de IA conversacional projetado para atuar como um especialista em engenharia de prompts. Ele guia os usuários por meio de um diálogo estruturado para ajudá-los a construir prompts claros, eficazes e otimizados para Modelos de Linguagem Grandes (LLMs).

O agente opera em duas fases:
1.  **Blueprint Estratégico:** Uma fase de descoberta interativa onde o agente faz perguntas direcionadas para entender completamente os requisitos do usuário.
2.  **Construção do Master Prompt:** Com base nas informações coletadas, o agente constrói um prompt completo e bem-estruturado, pronto para ser usado.

Este agente não utiliza ferramentas externas e depende exclusivamente de seu prompt de sistema e da capacidade de memória da conversa para guiar a interação.

## Como Executar

1.  **Instale as dependências:**
    Certifique-se de ter o `poetry` instalado. Em seguida, na raiz do diretório `prompt-architect`, execute:
    ```bash
    poetry install
    ```

2.  **Inicie uma conversa:**
    Você pode interagir com o agente usando a CLI do ADK ou um script Python.

    **Exemplo com a CLI do ADK:**
    ```bash
    adk web
    ```
    Em seguida, selecione o agente `prompt_architect` na lista.

O agente iniciará a conversa com sua saudação e o guiará pelo processo de criação do prompt.
