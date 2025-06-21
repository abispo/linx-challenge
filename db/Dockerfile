# base image
FROM postgres:11.20-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
