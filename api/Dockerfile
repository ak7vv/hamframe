FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim AS stage-1

LABEL org.opencontainers.image.source=https://github.com/ak7vv/hamframe
LABEL org.opencontainers.image.authors="Christian AK7VV <ak7vv@arrl.net>"
LABEL org.opencontainers.image.description="Hamframe API"
LABEL org.opencontainers.image.license=MIT

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

COPY requirements.txt .

RUN pip3 install --no-cache-dir --root-user-action ignore -r requirements.txt

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LOG_LEVEL=debug

COPY . .

ENTRYPOINT [ "python", "api.py" ]
