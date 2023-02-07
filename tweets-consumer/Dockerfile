FROM python:3.8-alpine3.11

RUN apk update && apk add build-base

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "run.py"]