# Use a base image with Python pre-installed
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 4444 available to the world outside this container
EXPOSE 4444

# Run app.py when the container launches
CMD ["python", "app.py"]
