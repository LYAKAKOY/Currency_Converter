# Конвертер валют

Api для Конвертера валют

## Стек программы
FastApi

## Как запустить проект
1. Требуется сделать git clone проекта
```bash
git clone https://github.com/LYAKAKOY/Currency_Converter
```
2. Собрать docker образ
```bash
docker build . -t 'currency_converter' 
```
3. Запустить docker образ
```bash
docker run -p 8000:8000 currency_converter
```
## Documentation
После запуска будет доступна
[Documentation](http://localhost:8000/docs) по адресу http://localhost:8000/docs


