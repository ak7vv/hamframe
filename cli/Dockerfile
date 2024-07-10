FROM alpine

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 py3-pip

WORKDIR /hamframe

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY cli.py cli.py

ENTRYPOINT ["python3", "cli.py"]
