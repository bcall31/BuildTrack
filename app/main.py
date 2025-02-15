from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import login
from core.db import Base, engine

import os

app = FastAPI(
    title="BuildTrack API",
    description="A Build Tracking Application",
    docs_url='/docs',
    openapi_url='/openapi.json',
    root_path='/'
)

app.include_router(login.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        os.environ.get("CORS_HOST", None)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
