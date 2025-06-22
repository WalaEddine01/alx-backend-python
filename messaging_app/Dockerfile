# Base Python image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the default Django port
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
