FROM alpine

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 py3-pip

WORKDIR /hamframe

COPY . .

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

# COPY /cli/cli.py /hamframe/cli.py

ENTRYPOINT ["python3", "cli.py"]
