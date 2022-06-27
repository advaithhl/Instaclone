# Dockerfile for the nginx server
FROM nginx:latest

# Copy nginx config file
COPY ./nginx_default.conf /etc/nginx/conf.d/default.conf
