from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Flexume! I don't do anything yet, just scaffolding."}