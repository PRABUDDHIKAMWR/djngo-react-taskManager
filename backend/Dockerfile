# Use official Python image
#FROM python:3.13-slim
FROM python:3.13-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/   
#or RUN mkdir -p /home/app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc \
    && apt-get autoremove -y


# Expose the Django port
EXPOSE 8000

#RUN chmod +x entrypoint.sh
#ENTRYPOINT ["entrypoint.sh"]

# Run Django’s development server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#RUN ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Stage 2: Production stage
#FROM python:3.13-slim

#RUN useradd -m -r appuser && \
#   mkdir /app && \
#   chown -R appuser /app

# Copy the Python dependencies from the builder stage
#COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
#COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
#WORKDIR /app
 
# Copy application code
#COPY --chown=appuser:appuser . .

# Set environment variables to optimize Python
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1 
 
# Switch to non-root user
#USER appuser

# Start the application using Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "my_docker_django_app.wsgi:application"]

