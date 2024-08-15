FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/django_backend

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONBUFFERED 1

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    netcat \
    libpq-dev \
    gcc \
    && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Prepare entrypoint script
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/django_backend/entrypoint.sh
RUN chmod +x /usr/src/django_backend/entrypoint.sh

# Copy the rest of the application code
COPY . .

# Set the entrypoint
ENTRYPOINT [ "/usr/src/django_backend/entrypoint.sh" ]

# FROM python:3.12.2-slim-bullseye

# WORKDIR /usr/src/django_backend

# ENV PYTHONDONTWRITEBYTECODE 1 
# ENV PYTHONBUFFERED 1

# RUN apt-get update && apt-get install -y netcat

# RUN pip install --upgrade pip

# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
# COPY ./entrypoint.sh .

# RUN sed -i 's/\r$//g' /usr/src/django_backend/entrypoint.sh
# RUN chmod +x /usr/src/django_backend/entrypoint.sh
# COPY . .

# ENTRYPOINT [ "/usr/src/django_backend/entrypoint.sh" ]



