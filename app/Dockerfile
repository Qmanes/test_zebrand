## set base image (host OS)
#FROM python
#
## set the working directory in the container
#WORKDIR /code
#
## copy the dependencies file to the working directory
#COPY requirements.txt .
#
## install dependencies
#RUN pip install -r requirements.txt
#
## copy the content of the local src directory to the working directory
#COPY .
#
## command to run on container start
#CMD [ "python", "server.py" ] 

FROM python:latest
RUN apt-get update
RUN apt-get -y upgrade

RUN pip install flask
RUN pip install mariadb
RUN pip install Flask-RESTful
RUN pip install email-validator
RUN pip install bcrypt
RUN pip install Flask-JWT-Extended
RUN pip install pytest
WORKDIR /server
CMD ["python", "server.py"]
