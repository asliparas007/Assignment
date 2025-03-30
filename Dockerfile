# Use the official Playwright image
FROM mcr.microsoft.com/playwright:v1.25.0-focal

# Install Python, pip, and xvfb
RUN apt-get update && apt-get install -y python3 python3-pip xvfb

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Install specific version of pyee
RUN pip install pyee==8.2.2

# Install Playwright and its dependencies
RUN pip install playwright
RUN playwright install

# Copy the entire project into the container
COPY . .

# Start Xvfb and run the tests
CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x24 & export DISPLAY=:99 && pytest -v tests/test_grafana.py"]
