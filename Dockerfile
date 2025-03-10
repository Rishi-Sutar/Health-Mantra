# Use the official Docker image
FROM docker:20.10.7-dind

# Install Docker Compose
RUN apk add --no-cache py-pip && pip install docker-compose

# Set the working directory
WORKDIR /app

# Copy the Docker Compose file and the application code
COPY docker-compose.yaml /app/docker-compose.yaml
COPY webapp /app/webapp
COPY calories-tracker /app/calories-tracker

# Expose the ports
EXPOSE 8000 5000

# Start Docker Compose
CMD ["docker-compose", "up"]