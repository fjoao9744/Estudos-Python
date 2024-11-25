import asyncio

def decorator(func: object) -> object:
    async def wrapper(*args: int, **kwargs: int) -> object:

        print("1")
        await asyncio.sleep(1)
        print("2")
        await asyncio.sleep(1)
        print("3")
        await asyncio.sleep(1)
        print("A resultado do seu calculo é: ", end="")
        await func(*args, **kwargs)

    return wrapper

@decorator
async def somar(n1: int = 0, n2: int = 0) -> None:
    print(n1 + n2)


if __name__ == "__main__":
    asyncio.run(somar(5, 4))
