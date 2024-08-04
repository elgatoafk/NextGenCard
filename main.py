import sys
import os
import uvicorn
import logging
from fastapi import FastAPI
from src.config.settings import settings
from src.util.base import Base, async_engine
from fastapi.middleware.cors import CORSMiddleware

# Ensure correct PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

# CORS Middleware setup, adjust as necessary
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all, checkfirst=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def on_startup():
    await init_db()


# Run the application
if __name__ == "__main__":
    debug_mode = os.getenv('DEBUG_MODE', 'False').lower() == 'true'
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=debug_mode)
