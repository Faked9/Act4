# Use Python 3.9 slim as the base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install Git and any necessary dependencies, then clean up
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the entire project into the container
COPY . /app

# Make entrypoint.sh executable
RUN chmod +x ./github/scripts/entrypoint.sh

# Set the entrypoint to run entrypoint.sh
ENTRYPOINT ["./github/scripts/entrypoint.sh"]

