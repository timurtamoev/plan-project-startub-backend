from fastapi import FastAPI

from routers import auth, features, how_it_works, pricing

app = FastAPI()

app.include_router(auth.router)
app.include_router(features.router)
app.include_router(how_it_works.router)
app.include_router(pricing.router)
