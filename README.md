# medical-iot-poc
A Proof of Concept demonstrating IoT integration for medical device data management.


# Medical IoT Proof of Concept

## Overview
This project demonstrates a proof of concept (PoC) for integrating IoT devices with medical data systems. It includes a simulated medical device, data ingestion via MQTT and InfluxDB, and visualisation with Grafana.

## Prerequisites
- **Python**: Version 3.9 or higher
- **Docker**: Installed and running
- **Git**: Installed on your system

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/dbuchalter/medical-iot-poc.git
cd medical-iot-poc
```

### Step 2: Prepare Docker Services

1. Start the Docker containers:
   ```bash
   docker-compose up -d
   ```
2. Confirm the services are running:
   ```bash
   docker ps
   ```

### Step 3: Set Up InfluxDB

1. Open InfluxDB at [http://localhost:8086](http://localhost:8086).
2. Create an admin user with the credentials:
   - **Username**: `admin`
   - **Password**: `admin123`
3. Set up the organisation:
   - **Name**: `medical-org`
4. Set up the bucket:
   - **Name**: `medical_devices`
5. Generate an API token for the bucket and replace `your-influxdb-token` in the provided scripts.

### Step 4: Simulate Device Data

1. Save the `device_simulator.py` script from the repository to your local machine.
2. Install dependencies:
   ```bash
   pip install paho-mqtt
   ```
3. Run the simulator:
   ```bash
   python device_simulator.py
   ```
4. Confirm the simulator is publishing data by checking the MQTT logs:
   ```bash
   docker logs mqtt_broker
   ```

### Step 5: Run the Data Ingestion Service

1. Save the `data_ingestion.py` script to your local machine.
2. Install dependencies:
   ```bash
   pip install paho-mqtt influxdb-client
   ```
3. Run the service:
   ```bash
   python data_ingestion.py
   ```
4. Verify that data is being ingested by checking the InfluxDB bucket.

### Step 6: Configure Grafana

1. Open Grafana at [http://localhost:3000](http://localhost:3000).
2. Log in using the default credentials:
   - **Username**: `admin`
   - **Password**: `admin`
3. Create a new data source:
   - Type: `InfluxDB`
   - URL: `http://influxdb:8086`
   - Database: `medical_devices`
4. Create a dashboard to visualise data.

## Troubleshooting

- **Docker Issues**: Run `docker-compose logs` to view logs for all services.
- **Python Errors**: Ensure all required libraries are installed.
- **InfluxDB Access**: Ensure InfluxDB is reachable at `http://localhost:8086`.

## Contributions
Feel free to fork the repository and submit pull requests for improvements or feature additions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

