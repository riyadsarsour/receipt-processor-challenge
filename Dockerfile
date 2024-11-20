FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements into the container and install dependencies, including curl
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y curl && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application files
COPY . .

# Expose the application port
EXPOSE 5002

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5002

# Start the Flask application
CMD ["python", "-m", "flask", "run"]
