FROM python:3.6-alpine

COPY loginTrackerServer /opt/loginTracker

WORKDIR /opt/loginTracker

RUN pip install virtualenv && \
    virtualenv .env && \
    source .env/bin/activate && \
    pip install -r requirements.txt

ENTRYPOINT ["sh", "-c", "source .env/bin/activate; python ./manage.py runserver 0.0.0.0:4242"]
