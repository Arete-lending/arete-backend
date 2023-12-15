# ./Dockerfile 
FROM python:3.9.1-alpine3.13
USER root
WORKDIR /app/backend
ENV TZ=Asia/Seoul

EXPOSE 8000

## Install packages
COPY ../requirements.txt ./
RUN python -m pip install -r requirements.txt

COPY .. .

CMD ["python", "start.py"]
