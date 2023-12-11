# ./Dockerfile 
FROM python:3.9.1
USER root
WORKDIR /app/backend
ENV TZ=Asia/Seoul

EXPOSE 8000

## Install packages
RUN pip install --upgrade pip
COPY ../requirements.txt ./
RUN pip install -r requirements.txt
## Copy all src files
COPY .. .

## Run the application on the port 8080
CMD python start.py
