# syntax=docker/dockerfile:1
FROM python:3.11.2-alpine

# Set working directory and environment variables
WORKDIR /app
ENV PORT=3000
ENV API_URL="https://swapi.dev/api/films/"

# Copy project source files into container
COPY src src/
COPY requirements.txt .

# Install required packages
RUN pip install -r requirements.txt

# Set the port to expose from within the container
EXPOSE 3000

# Run Flask server
CMD ["python", "-m", "src.router"]