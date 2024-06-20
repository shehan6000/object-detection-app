# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --upgrade pip
RUN pip install tensorflow tensorflow-hub opencv-python-headless

# Run app.py when the container launches
CMD ["python", "app.py"]

