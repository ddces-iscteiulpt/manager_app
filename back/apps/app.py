from fastapi import FastAPI

from routes.items import router as ItemsRouter

app = FastAPI()

app.include_router(ItemsRouter, tags=["Items"], prefix="/items")

@app.get("/", tags=["Root"])
async def read_root():
    return {"Hello": "World"}
