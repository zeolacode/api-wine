# Use the Python 3.11-bullseye base image
FROM python:3.11-bullseye

# Set the working directory inside the container
WORKDIR /app

# Update the package lists and install the libgomp1 package
RUN apt-get update && apt-get install -y libgomp1 && apt-get clean

COPY requirements.txt .

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire current directory into the container at /app
COPY app/ .

# Expose port 8000 to allow external access
EXPOSE 8000

# Set the command to run when the container starts
CMD ["python", "main.py"]
