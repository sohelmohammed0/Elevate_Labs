# Use official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only requirements first for better caching
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app/ .

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
