FROM ubuntu:24.04

WORKDIR /hamframe
COPY requirements.txt ./

RUN apt-get update && apt-get upgrade --yes
# RUN apt-get install --yes python3 python-is-python3 python3-pip python3-redis
# RUN pip install --break-system-packages --no-cache-dir -r requirements.txt
RUN apt-get install --yes python-is-python3 python3-redis

COPY cli.py .
CMD [ "python", "./cli.py" ]
