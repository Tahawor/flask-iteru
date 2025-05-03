# Use a minimal Python base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install OpenCV dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 5000

# Use gunicorn to run Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
