# based on https://fastapi.tiangolo.com/deployment/docker

FROM tiangolo/uvicorn-gunicorn-fastapi

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

COPY requirements.txt ./

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY api.py .

EXPOSE 8000

#ENTRYPOINT [ "fastapi", "run", "api.py", "--proxy-headers", "--port", "8000" ]
ENTRYPOINT [ "fastapi", "run", "api.py", "--proxy-headers", "--port", "8000" ]
