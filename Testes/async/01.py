import asyncio

async def tarefa_assincrona():
    print("Iniciando tarefa...")
    await asyncio.sleep(2)  # Simula uma pausa de 2 segundos (tarefa demorada)
    print("Tarefa concluída!")

async def main():
    print("Antes da tarefa")
    await tarefa_assincrona()  # Espera até que a tarefa seja concluída
    print("Após a tarefa")

# Rodando o programa
asyncio.run(main())
