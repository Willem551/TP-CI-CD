FROM python:3.13.5-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pylint

CMD ["python", "-m", "unittest", "discover"]
