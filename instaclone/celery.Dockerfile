# Dockerfile for the celery server.
FROM python:3.10.5-slim-buster

# Create app directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Copy code
COPY . /usr/src/app/

# Expose RabbitMQ port
EXPOSE 5672

# Run celery server
ENTRYPOINT [ "./celery.docker-entrypoint.sh" ]
