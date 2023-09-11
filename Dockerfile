# Use a base image with Python pre-installed
FROM python:3.10

# Create a working directory in the container
WORKDIR /app

# Copy your Flask application code into the container
COPY . .

# Expose the port your Flask app is listening on (default is 5000)
EXPOSE 5000

# Define the command to run your Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
