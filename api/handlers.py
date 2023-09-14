from typing import Dict
from .models import Currency
from fastapi import APIRouter, Query
from converter_currency import convert_currency


currency_router = APIRouter()


odd_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "example": {
                        "value": '{ "result": 62.16 }'
                    }
                },
            }
        }
    },
}


@currency_router.get("/rates", response_model=Dict[str, float], responses=odd_responses)
async def get_rates(from_: Currency = Query(..., description="Исходная валюта", min_length=3, max_length=3),
                    to: Currency = Query(..., description="Целевая валюта", min_length=3, max_length=3),
                    value: float = Query(..., description="Сумма для конвертации", gt=0)) -> Dict[str, float]:
    result = await convert_currency(from_, to, value)
    return {"result": result}
