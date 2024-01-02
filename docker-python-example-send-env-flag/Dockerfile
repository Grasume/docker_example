FROM python:3.10-slim

# Path: /app
WORKDIR /app

COPY . .

ENV IMAGE_PATH=test

CMD python ./test.py -IMAGE=$IMAGE_PATH