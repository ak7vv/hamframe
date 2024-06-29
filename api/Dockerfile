FROM alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /hamframe

RUN apk add --update --nocache python3 py3-pip

COPY requirements.txt ./

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY api.py .

ENTRYPOINT [ "gunicorn", "-w", "20", "-b", "0.0.0.0:8000", "flask.py:flaskfile" ]
