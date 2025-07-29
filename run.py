import os
import asyncio
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path='../../../../../.env')

# É crucial configurar a API Key *antes* de importar o agente,
# pois o modelo da Google é inicializado no momento da importação.
from google.adk.models.generative_ai import GenerativeAi
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("A variável de ambiente GEMINI_API_KEY não foi encontrada.")
GenerativeAi.configure(api_key=api_key)

# Agora, importa o agente
from prompt_architect import root_agent

async def main():
    """Inicia um loop de chat interativo com o agente no terminal."""
    print("Iniciando o chat com o Prompt Architect. Digite 'sair' para terminar.")
    print("-" * 30)

    # O ADK mantém o histórico da conversa internamente no agente.
    # A cada chamada de `agent.send()`, o novo turno é adicionado à memória.
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Encerrando o chat. Até logo!")
            break

        if not user_input.strip():
            continue

        try:
            # Envia a mensagem para o agente e espera a resposta
            response_generator = root_agent.send(user_input)
            
            # Itera sobre a resposta do gerador para obter a mensagem final
            final_response = ""
            async for chunk in response_generator:
                final_response = chunk.text
            
            print(f"Agente: {final_response}")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            # Em caso de erro, você pode querer reiniciar o loop ou sair
            break

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nChat interrompido pelo usuário.") 