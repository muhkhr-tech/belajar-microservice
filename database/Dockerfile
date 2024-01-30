# cat Dockerfile
FROM mysql:8

RUN chown -R mysql:root /var/lib/mysql/

ENV MYSQL_DATABASE=products_db
ENV MYSQL_USER=rafiq
ENV MYSQL_PASSWORD=rafiq
ENV MYSQL_ROOT_PASSWORD=root

COPY init.sql /docker-entrypoint-initdb.d

EXPOSE 3306