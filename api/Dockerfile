FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11 AS stage-1

LABEL org.opencontainers.image.source=https://github.com/ak7vv/hamframe
LABEL org.opencontainers.image.authors="Christian AK7VV <ak7vv@arrl.net>"
LABEL org.opencontainers.image.description="Hamframe API"
LABEL org.opencontainers.image.license=MIT

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

# RUN apt-get update && \
#     apt-get upgrade --yes && \
#     apt-get autoremove --yes && \
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



FROM stage-1 AS stage-2

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

COPY requirements.txt .

#RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt



FROM stage-1

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

COPY --from=stage-2 /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=stage-2 /usr/local/bin /usr/local/bin

# copy everything explicitly 'allowed' in .dockerignore
COPY . .

# set defaults
ARG REDIS_HOST_DEFAULT=localhost
ARG REDIS_PORT_DEFAULT=6379

# let user override
ENV REDIS_HOST=${REDIS_HOST_DEFAULT}
ENV REDIS_PORT=${REDIS_PORT_DEFAULT}

ENTRYPOINT [ "python", "api.py" ]
