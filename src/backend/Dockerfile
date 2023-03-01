FROM python:3.9

WORKDIR /app/backend

RUN ls

COPY ./migrations ./migrations
COPY ./shopbridge ./shopbridge
COPY ./tests ./tests
COPY ./config.py ./config.py
COPY ./requirements.txt ./requirements.txt
COPY ./wsgi.py ./wsgi.py

RUN pip install -r requirements.txt

ENV FLASK_ENV production

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]

