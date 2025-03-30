# Automated UI Testing with Playwright for Grafana

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Docker (for running Grafana and tests)

### Installation
1. Clone this repository:
   ```sh
   git clone 

   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```sh
   playwright install --with-deps
   ```

## Running Tests

### Running Locally
1. Start a local Grafana instance:
   ```sh
   docker run -d -p 3000:3000 grafana/grafana
   ```
2. Run the test script:
   ```sh
   pytest tests/test_grafana.py
   ```

### Running with Docker
1. Build the Docker image:
   ```sh
   docker build -t playwright-grafana .
   ```
2. Run the container:
   ```sh
   docker run --rm playwright-grafana
   ```

## Expected Output
- A new Grafana dashboard is created.
- A Timeseries visualization is generated.
- A screenshot is taken and compared against a reference image.
- The test passes if the comparison is successful.

## Notes
- Ensure the `reference_screenshot.png` is available in the project.
- Modify the test script if running with different Grafana configurations.
