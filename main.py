from fastapi import FastAPI
from app.routes import issues_router
from app.middleware.timer import timing_middleware

app = FastAPI()


@app.get("/health")
async def health_check():
    """
    Endpoint to confirm api is running
    """
    return {"status": "ok"}


app.middleware("http")(timing_middleware)
app.include_router(issues_router)
