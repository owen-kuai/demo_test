FROM python:3.6

RUN mkdir /demo_test

WORKDIR /demo

COPY ./requirements.txt /demo_test

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ca-certificates curl supervisor ca-certificates nginx vim

COPY . /demo_test

CMD ["python", "demo_test.py"]


EXPOSE 5000