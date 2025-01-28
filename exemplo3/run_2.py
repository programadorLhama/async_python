from fastapi import FastAPI
import uvicorn
import asyncio

app = FastAPI()

@app.get("/")
async def read_root():
    await asyncio.sleep(20)
    return { "hello": "world" }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
