from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import databases
from sqlalchemy import MetaData, Table, Column, Integer, String

# Criar a conexão
DATABASE_URL = "sqlite:///./schema.db"
database = databases.Database(DATABASE_URL)

# Descrever tabelas
metadata = MetaData()
PESSOA = Table(
    "pessoas", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)

# Fazer query
async def get_all_people():
    query = PESSOA.select()
    result = await database.fetch_all(query)
    return result

app = FastAPI()
@app.get("/")
async def read_data():
    await database.connect()
    people = await get_all_people()
    print(people)

    formatted_pessoas = []
    for pessoa in people:
        formatted_pessoas.append(pessoa.name)

    await database.disconnect()
    return JSONResponse(
        content={ "pessoas": formatted_pessoas },
        status_code=200
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)