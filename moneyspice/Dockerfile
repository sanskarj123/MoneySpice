# base image 
FROM python:3.8
#set environment variable
ENV PYTHONUNBUFFERED=1
# create and set work directory
RUN mkdir /app/
WORKDIR /app
COPY . /app/
# copy and install all the dependencies
COPY requirements.txt /code/
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

# uWSGI will listen on this port
EXPOSE 8000