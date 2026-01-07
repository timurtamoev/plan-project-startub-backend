from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, features, how_it_works, pricing

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(features.router)
app.include_router(how_it_works.router)
app.include_router(pricing.router)
