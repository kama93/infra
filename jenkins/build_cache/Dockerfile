FROM nginx:latest

# install extras
RUN apt -y update
RUN apt install -y nginx-extras

RUN mkdir -p /cache
RUN chown -R www-data:www-data /cache

COPY cache_site.conf /etc/nginx/conf.d
