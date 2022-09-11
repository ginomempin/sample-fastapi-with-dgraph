from fastapi import FastAPI

app = FastAPI()


@app.get("/data")
async def get_data():
    return {"total_items": 0, "items": []}
