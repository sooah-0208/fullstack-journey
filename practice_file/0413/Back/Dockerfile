# syntax=docker/dockerfile:1
FROM python:3.13.11

WORKDIR /app

# install uv
RUN pip install uv

COPY pyproject.toml uv.lock* ./
RUN uv pip install --system -r pyproject.toml

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
