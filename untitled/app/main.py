from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.health import router as health_router
from app.api.v1.leaderboard import router as leaderboard_router

app = FastAPI(
    title="Unity Game Backend"
)

app.include_router(
    auth_router,
    prefix="/api/v1"
)

app.include_router(
    health_router,
    prefix="/api/v1"
)

app.include_router(
    leaderboard_router,
    prefix="/api/v1"
)


@app.get("/")
async def root():
    return {
        "message": "Backend running"
    }