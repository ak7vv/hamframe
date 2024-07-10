FROM alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

RUN apk add --update --no-cache python3 py3-pip

COPY requirements.txt /hamframe/requirements.txt

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY cli.py .

ENTRYPOINT ["python3", "cli.py"]
