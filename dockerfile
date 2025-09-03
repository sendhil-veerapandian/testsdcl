FROM python:3.12-slim-bookworm

# Prevent Python from writing .pyc files to disk and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt /app/

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app source code
COPY . /app/

# Cloud Run requires the app to listen on $PORT
ENV PORT=8080

EXPOSE 8080

# Start the app
CMD ["python", "app_api.py"]
