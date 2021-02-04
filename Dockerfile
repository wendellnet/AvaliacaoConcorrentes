FROM python:alpine3.7

EXPOSE 5000

ENTRYPOINT ["gunicorn"]

CMD ["--workers=4", "--bind=0.0.0.0:5000", "app:my_app"]

RUN mkdir /ac_api && \
    apk upgrade --update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev && \
    pip install pipenv

COPY . /ac_api
WORKDIR /ac_api

RUN pipenv install --system --deploy
