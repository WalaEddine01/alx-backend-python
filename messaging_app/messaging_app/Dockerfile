# Use base Python image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose the Django port
EXPOSE 8000

# Note: Port is exposed via Docker run command
# Example: docker run -p 8000:8000 messaging_app_image ✅

# Start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
