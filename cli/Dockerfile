From alpine

WORKDIR /hamframe

RUN apk add --update --no-cache python3 py3-pip

COPY requirements.txt ./

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY cli.py .

CMD [ "python3", "./cli.py" ]
