from fastapi import FastAPI
from app.routes import issues_router

app = FastAPI()


@app.get("/health")
async def health_check():
    """
    Endpoint to confirm api is running
    """
    return {"status": "ok"}


app.include_router(issues_router)
