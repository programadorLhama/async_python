import asyncio

# coroutine
async def say_hello(name):
    print(f"{name} is starting...")
    await asyncio.sleep(2) # Simulando IO
    print(f"{name} says hello")

# coroutine
async def main():
    await say_hello("Larissa") # atuação sincrona
    await asyncio.gather(
        say_hello("Lhama"),
        say_hello("Rogerio"), # atuação assincrona
    )

asyncio.run(main())
