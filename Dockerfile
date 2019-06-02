FROM python:3.6-alpine

COPY loginTrackerServer /opt/loginTracker

WORKDIR /opt/loginTracker

RUN pip install virtualenv \
    && virtualenv .env \
    && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev \
    && pip install --no-cache-dir psycopg2 \
    && apk del --no-cache .build-deps \
    && source .env/bin/activate \
    && pip install -r requirements.txt


ENTRYPOINT ["sh", "-c", "source .env/bin/activate; python ./manage.py runserver 0.0.0.0:4242"]
