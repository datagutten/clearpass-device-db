FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY wifi.crt /etc/nginx/ssl/wifi.crt
COPY wifi.key /etc/nginx/ssl/wifi.key
