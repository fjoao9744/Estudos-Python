import asyncio

def destacar(func: object) -> object:
    async def wrapper(*args: int, **kwargs: int) -> object:
        print("-" * 20)
        await func(*args, **kwargs)
        print("-" * 20)
        
    return wrapper

@destacar
async def soma(*args: int) -> None:
    final_num = 0
    for _ in args:
        final_num += _
        
    print(final_num)

if __name__ == "__main__":
    asyncio.run(soma(2, 5, 1,9,9,9,9,7,6,5,0,-88, 20, 10))
