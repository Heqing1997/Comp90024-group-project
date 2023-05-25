FROM python:3.11

WORKDIR /flask

COPY . /flask

RUN pip install couchdb;\
    pip install flask-cors;\
    pip install flask


EXPOSE 8080

CMD ["python", "./backend/app.py"]