FROM nginx:latest

COPY ./nginx.conf /etc/nginx/

ARG apt_password

RUN apt update
RUN apt -y install apache2-utils
RUN mkdir -p /etc/apache2/ && htpasswd -b -c /etc/apache2/apt_htpasswd apt ${apt_password}
