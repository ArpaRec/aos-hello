# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy the app code
COPY app.py /app/

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
