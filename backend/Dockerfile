FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4800

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4800"]