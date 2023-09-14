import aiohttp
from bs4 import BeautifulSoup as bs

from api.models import Currency


def normalize_rate(amount: str) -> float:
    all_part_of_amount = amount.split('.')
    normalize_amount = int(all_part_of_amount[0])
    for part_amount in all_part_of_amount[1:-1]:
        normalize_amount *= 1000
        normalize_amount += int(part_amount)
    normalize_amount = f"{normalize_amount}.{all_part_of_amount[-1]}"
    return float(normalize_amount)


def get_rate(content: str) -> str | None:
    soup = bs(content, "html.parser")
    price_datetime = soup.find("span", class_="ccOutputRslt")
    return price_datetime.text


async def get_content_rates(from_currency: Currency, to_currency: Currency, value: float) -> str | None:
    url = f"https://www.x-rates.com/calculator/?from={from_currency.value}&to={to_currency.value}&amount={value}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def convert_currency(from_: Currency, to: Currency, value: float) -> float:
    content = await get_content_rates(from_, to, value)
    amount = get_rate(content).replace(',', '.').split(' ')[0]
    return normalize_rate(amount)
