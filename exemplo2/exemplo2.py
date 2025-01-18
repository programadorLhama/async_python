import asyncio
import httpx

async def fetch_get(client: any, pokemon_name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = await client.get(url) # I/O
    data = response.json()

    name = data["name"]
    hability = data["moves"][0]["move"]
    print(f"name: {name} / move: {hability}")
    print()
    print()


async def main():
    async with httpx.AsyncClient() as client:
        await fetch_get(client, "ditto")
        await asyncio.gather(
            fetch_get(client, "charizard"),
            fetch_get(client, "mew"),
        )
        print("Acabei!")

asyncio.run(main())
