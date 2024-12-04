FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY app.py ./app.py

RUN apk add --no-cache build-base
RUN pip install -r requirements.txt


ENTRYPOINT [ "python" ]

CMD ["./app.py" ]