# based on https://fastapi.tiangolo.com/deployment/docker

FROM tiangolo/uvicorn-gunicorn-fastapi

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

COPY /api/requirements.txt /hamframe/requirements.txt

RUN pip3 install --break-system-packages --no-cache-dir -r /hamframe/requirements.txt

COPY /api/api.py /hamframe/api.py
COPY /api/api.sh /hamframe/api.sh

COPY /api/configuration/ /hamframe/

COPY /api/database/ /hamframe/

EXPOSE 8000

ENTRYPOINT [ "sh", "/hamframe/api.sh" ]
