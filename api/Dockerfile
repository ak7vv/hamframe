# based on https://fastapi.tiangolo.com/deployment/docker

FROM tiangolo/uvicorn-gunicorn-fastapi

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

COPY . .

# COPY /api/requirements.txt /hamframe/requirements.txt

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

# COPY /api/api.py /hamframe/api.py
# COPY /api/api.sh /hamframe/api.sh

# RUN mkdir /hamframe/configuration

# RUN mkdir /hamframe/database

# COPY /api/configuration/* /hamframe/configuration/

# COPY /api/database/* /hamframe/database/

# set defaults
ARG REDIS_HOST_DEFAULT=localhost
ARG REDIS_PORT_DEFAULT=6379
ARG WORKERS_DEFAULT=4

# let user override
ENV REDIS_HOST=${REDIS_HOST_DEFAULT}
ENV REDIS_PORT=${REDIS_PORT_DEFAULT}
ENV WORKERS=${WORKERS_DEFAULT}

# ENTRYPOINT [ "sh", "/hamframe/api.sh" ]
ENTRYPOINT ["gunicorn", "--workers", "${WORKERS}" ]
