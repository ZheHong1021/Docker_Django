# Use an official Python runtime as a parent image
FROM python:3.9.12

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
# 將 pip install 進行更新
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Expose the port the app will run on
EXPOSE 8000

# Copy the project code into the container
COPY . /app/