FROM python:3-alpine

WORKDIR /hamframe
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./cli.py" ]
