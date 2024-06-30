# based on https://fastapi.tiangolo.com/deployment/docker

FROM tiangolo/uvicorn-gunicorn-fastapi

ENV PYTHONUNBUFFERED=1

RUN mkdir /hamframe /hamframe/configuration

WORKDIR /hamframe

COPY requirements.txt /hamframe/requirements.txt

RUN pip3 install --break-system-packages --no-cache-dir -r /hamframe/requirements.txt

COPY api.py api.sh /hamframe

COPY configuration/* /hamframe/configuration

EXPOSE 8000

ENTRYPOINT [ "sh", "/hamframe/api.sh" ]
