# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim AS stage-1
FROM python:slim AS stage-1

LABEL org.opencontainers.image.source=https://github.com/ak7vv/hamframe
LABEL org.opencontainers.image.authors="Christian AK7VV <ak7vv@arrl.net>"
LABEL org.opencontainers.image.description="Hamframe API"
LABEL org.opencontainers.image.license=MIT

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

# prereq for couchbase python sdk

RUN apt-get update && \
    apt-get upgrade --yes && \
    apt install --yes apt-utils

# Get the Python version and store it in a file
RUN python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" > /python_version
RUN cat /python_version

    
FROM stage-1 AS stage-2

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

RUN cat /python_version

RUN apt-get install --yes \
        ccache \
        cmake \
        g++ \
        git \
        libssl-dev \
        zlib1g-dev

# upgrade pip just in case
RUN pip3 install --upgrade pip

# build couchbase wheel

RUN pip3 install --no-cache-dir ---root-user-action couchbase



FROM stage-2 AS stage-3

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

RUN cat /python_version

COPY requirements.txt .

RUN pip3 install --no-cache-dir --root-user-action -r requirements.txt

# remove unneccessary stuff
RUN apt-get remove --yes \
        ccache \
        cmake \
        g++ \
        git \
        libssl-dev \
        zlib1g-dev \
        && \
    apt-get autoremove --yes



FROM stage-1 AS stage-4

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

# Read the Python version into an ARG
COPY --from=stage-1 /python_version /python_version
ARG PYTHON_VERSION
RUN cat /python_version
RUN PYTHON_VERSION=$(cat /python_version)

COPY --from=stage-3 /usr/local/lib/python${PYTHON_VERSION}/site-packages /usr/local/lib/python${PYTHON_VERSION}/site-packages
COPY --from=stage-3 /usr/local/bin /usr/local/bin

# copy everything explicitly 'allowed' in .dockerignore
COPY . .

# set defaults
ARG REDIS_HOST_DEFAULT=localhost
ARG REDIS_PORT_DEFAULT=6379
ARG LISTENER_HOST_DEFAULT=0.0.0.0
ARG LISTENER_PORT_DEFAULT=65432
ARG LISTENER_WORKERS_DEFAULT=4

# let user override defaults
ENV REDIS_HOST=${REDIS_HOST_DEFAULT}
ENV REDIS_PORT=${REDIS_PORT_DEFAULT}
ENV LISTENER_HOST=${LISTENER_HOST_DEFAULT}
ENV LISTENER_PORT=${LISTENER_PORT_DEFAULT}
ENV LISTENER_WORKERS=${LISTENER_WORKERS_DEFAULT}

ENTRYPOINT [ "python", "api.py" ]
