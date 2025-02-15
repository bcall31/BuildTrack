# Use official Python image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl gnupg2 unixodbc unixodbc-dev

# Add Microsoft ODBC repository and install ODBC Driver 17
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17


# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (to leverage Docker caching)
COPY requirements.txt .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application
COPY . .

# Command to run the application
CMD uvicorn main:app --host 0.0.0.0 --port 80
