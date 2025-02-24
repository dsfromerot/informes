# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5003

# Command to run the application
# For development, use Flask's built-in server:
CMD ["flask", "run", "--host=0.0.0.0", "--port=5003"]

# For production, use Gunicorn (uncomment the line below if using gunicorn):
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5003", "app:app"]
