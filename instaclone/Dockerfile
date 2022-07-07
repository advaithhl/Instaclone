# Dockerfile for the Django app and gunicorn app server.
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

# Expose app server
EXPOSE 8000

# Run app server
ENTRYPOINT [ "./docker-entrypoint.sh" ]
