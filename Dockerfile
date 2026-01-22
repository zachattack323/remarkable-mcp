FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FASTMCP_HOST=0.0.0.0

WORKDIR /app

# System deps for cairo/pango/tesseract (OCR/rendering)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libcairo2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libgdk-pixbuf-xlib-2.0-0 \
        libffi-dev \
        tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir .

# Cloud Run sends traffic to $PORT; entrypoint maps it to FASTMCP_PORT
CMD ["python", "cloud_run_entrypoint.py"]
