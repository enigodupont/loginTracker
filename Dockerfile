FROM python:3.6-alpine

COPY loginTrackerServer /opt/loginTracker

WORKDIR /opt/loginTracker

RUN pip install virtualenv \
    && virtualenv .env \
    && source .env/bin/activate \
    && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev \
    && pip install --no-cache-dir  -r requirements.txt \
    && apk del --no-cache .build-deps


ENTRYPOINT ["sh", "-c", "source .env/bin/activate; python ./manage.py runserver 0.0.0.0:4242"]