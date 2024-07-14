### stage 1: build prereq
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11 AS prereq

LABEL org.opencontainers.image.source=https://github.com/ak7vv/hamframe
LABEL org.opencontainers.image.descriptiob="Hamframe API"
LABEL org.opencontainers.image.license=MIT

# if python burps, we want to see it immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

COPY requirements.txt .

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --break-system-packages -r requirements.txt



### stage 2: app
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# if python burps, we want to see it immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

# populate prereq's from stage 1
COPY --from=prereq /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=prereq /usr/local/bin /usr/local/bin

# copy everything explicitly 'allowed' in .dockerignore
COPY . .

# set defaults
ARG REDIS_HOST_DEFAULT=localhost
ARG REDIS_PORT_DEFAULT=6379

# let user override
ENV REDIS_HOST=${REDIS_HOST_DEFAULT}
ENV REDIS_PORT=${REDIS_PORT_DEFAULT}

ENTRYPOINT [ "python", "api.py" ]
