FROM python:3

WORKDIR /flask-market

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 -w 3 wsgi:app