FROM nginx:latest

COPY ./nginx.conf /etc/nginx/

RUN apt update
RUN apt -y install apache2-utils
RUN mkdir -p /etc/apache2/
