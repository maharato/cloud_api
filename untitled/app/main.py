from contextlib import asynccontextmanager
from fastapi import FastAPI

# 1. Import your database tools and MODELS
# IMPORTANT: You must import your models here so SQLAlchemy "sees" them
from app.core.database import engine, Base
from app.models.player import Player # <--- Make sure this import exists!

from app.api.v1.auth import router as auth_router
from app.api.v1.health import router as health_router
from app.api.v1.leaderboard import router as leaderboard_router
from app.api.v1.progress import router as progress_router
from app.api.v1.story import router as story_router

# 2. Define the lifespan to create tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs when the app starts
    async with engine.begin() as conn:
        # This creates 'players' table if it's missing
        await conn.run_sync(Base.metadata.create_all)
    yield

# 3. Initialize the app WITH the lifespan
app = FastAPI(
    title="Unity Game Backend",
    lifespan=lifespan
)

# ... your router includes ...
app.include_router(auth_router, prefix="/api/v1")
app.include_router(health_router, prefix="/api/v1")
app.include_router(leaderboard_router, prefix="/api/v1")
app.include_router(progress_router, prefix="/api/v1")
app.include_router(story_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Backend running"}

if __name__ == "__main__":
    import uvicorn
    # Make sure the string "main:app" matches your filename
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)