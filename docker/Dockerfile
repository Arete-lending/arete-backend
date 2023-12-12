# ./Dockerfile 
FROM nginx:stable
USER root
WORKDIR /app/backend
ENV TZ=Asia/Seoul

EXPOSE 80
EXPOSE 443
EXPOSE 8000

RUN apt-get update
RUN apt-get install -y python3.9 \
    && ln -s /usr/bin/python3.9 /usr/bin/python3 \
    && ln -s /usr/bin/python3.9 /usr/bin/python
ENV PATH="$PATH:/usr/bin:/usr/local/bin"
RUN apt-get install -y pip
## Install packages
RUN python -m pip install --upgrade pip
COPY ../requirements.txt ./
RUN python -m pip install -r requirements.txt

COPY .. .

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/nginx.conf /etc/nginx/conf.d

CMD ["python", "start.py"]
