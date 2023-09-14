from fastapi import FastAPI, APIRouter
from api.handlers import currency_router

app = FastAPI(title="currency converter")

main_api_router = APIRouter()

main_api_router.include_router(currency_router, prefix="/api", tags=["api"])
app.include_router(main_api_router)

