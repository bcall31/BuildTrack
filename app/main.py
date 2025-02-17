from fastapi import FastAPI #type: ignore
from fastapi.middleware.cors import CORSMiddleware #type: ignore
from router import account, auth, user
from core.db import InitDB

import os


app = FastAPI(
    title="BuildTrack API",
    description="A Build Tracking Application",
    docs_url='/docs',
    openapi_url='/openapi.json',
    root_path='/'
)
@app.on_event("startup")
def on_startup():
    InitDB() 

app.include_router(account.router, tags=["Login and Registration"])
app.include_router(auth.router, tags=["Authentication"])
app.include_router(user.router, tags=["User Management"])


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
