FROM python:3.11-alpine3.18

WORKDIR /web_app

COPY requirements.txt /temp/requirements.txt

EXPOSE 8000

RUN pip install -r /temp/requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]