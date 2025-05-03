# Use a lightweight Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install system dependencies needed by OpenCV and clean up
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port defined by Railway (defaults to 8080, configurable)
EXPOSE $PORT

# Run the Flask app with Gunicorn, using environment variable PORT
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "--workers=1", "--timeout=120", "--log-level=debug", "app:app"]