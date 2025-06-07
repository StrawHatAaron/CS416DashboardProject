# Use the latest official Python 3 image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy any local files (optional)
COPY . /app

# Install pandas
RUN pip install --no-cache-dir pandas

# Define the default command
CMD ["python3", "mine_BLS.py"]
