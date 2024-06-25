FROM ubuntu:24.04

WORKDIR /hamframe
COPY requirements.txt ./
COPY cli.py .

RUN apt-get update && apt-get upgrade --yes
RUN apt-get install --yes python3-dev python-is-python3 python3-pip python3-redis
RUN pip install --break-system-packages --no-cache-dir -r requirements.txt

CMD [ "python", "./cli.py" ]
