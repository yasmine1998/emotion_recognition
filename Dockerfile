# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy the script and other necessary files to the working directory
COPY fer.py .
COPY emojis/happy1.png .
COPY emojis/happy2.png .
COPY emojis/sad1.png .
COPY emojis/sad2.png .
COPY emojis/fear1.png .
COPY emojis/fear2.png .
COPY emojis/disgust1.png .
COPY emojis/disgust2.png .
COPY emojis/angry1.png .
COPY emojis/angry2.png .
COPY emojis/surprise1.png .
COPY emojis/neutral1.png .

# Install dependencies
RUN pip install opencv-python deepface

# Run the script when the container launches
CMD ["python3", "fer.py"]
