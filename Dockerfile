FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y libpq-dev
RUN pip3 install --upgrade pip
RUN pip3 install django
RUN pip3 install reportlab==3.6.10
COPY . .
CMD python3 manage.py runserver 0.0.0.0:8000