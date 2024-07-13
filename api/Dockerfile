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

# set default to 65432/tcp and allow user to override with API_PORT environment variable
ARG API_PORT_DEFAULT=65432
ENV API_PORT=${API_PORT_DEFAULT}

# ENTRYPOINT [ "sh", "/hamframe/api.sh" ]
ENTRYPOINT ["gunicorn", "--workers, "4", "--port", "${API_PORT_DEFAULT}"]
