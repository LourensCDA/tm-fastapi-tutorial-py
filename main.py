from fastapi import FastAPI
from app.routes import issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/health")
async def health_check():
    """
    Endpoint to confirm api is running
    """
    return {"status": "ok"}


app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(issues_router)
