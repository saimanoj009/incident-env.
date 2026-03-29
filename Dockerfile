FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt || true

# Expose port
EXPOSE 8000

CMD ["python", "-m", "server.app"]
