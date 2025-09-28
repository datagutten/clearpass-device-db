FROM ghcr.io/datagutten/clearpass-device-db AS static
RUN python /home/app/manage.py collectstatic --noinput

FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx_nossl.conf /etc/nginx/conf.d

COPY --from=static /home/app/static /home/app/static