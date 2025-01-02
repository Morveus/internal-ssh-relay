# Use Python base image
FROM python:3.9-slim

# Install sshpass
RUN apt-get update && \
    apt-get install -y sshpass && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY run.py .

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]
