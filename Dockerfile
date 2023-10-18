# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port that Uvicorn will run on (default is 8000)
EXPOSE 8000

# Use the full path to the Uvicorn executable
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]