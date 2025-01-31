import asyncio
from src.model.settings.db_connection_handler import db_connection_handler
from src.model.repositories.pessoas_repository import PessoasRepository

async def run_people():
    await db_connection_handler.connect_to_db()

    repo = PessoasRepository()
    pessoas = await repo.get_all_people()

    for pessoa in pessoas:
        print(pessoa.name)

    await db_connection_handler.disconnect_to_db()


asyncio.run(run_people())
