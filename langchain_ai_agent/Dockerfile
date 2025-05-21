# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Make port 80 available to the world outside this container (if needed for future web apps, not strictly for this script)
# EXPOSE 80

# Define environment variable for OpenAI API Key (to be passed at runtime)
ENV OPENAI_API_KEY=""

# Run agent.py when the container launches
CMD ["python", "agent.py"]
