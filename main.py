from fastapi import FastAPI
from app.routes.applications import router as applications_router

app = FastAPI(title="BIG Invest API")

app.include_router(applications_router)
