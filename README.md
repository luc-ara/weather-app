# Weather Data Collector

A simple Python script to retrieve weather data from the Open-Meteo API and store it in JSON Lines format.

This project is an exercise for learning API consumption, data storage, and data manipulation.

## Current Features
- Retrieves current weather data from Open-Meteo.
- Accepts an external JSON configuration file.
- Stores observations in a separate JSON Lines file for each day.

## Requirements
- Python 3.10 or newer

## Installation and Usage
Clone the repository:
```bash
git clone <url>
cd weather-app
```
Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the script:
```bash
python weather_app.py
```

## Configuration
The script requires a file named `config.json` located in the project's directory.
- `reports_dir`: The folder in which report files will be stored.
- `title_prefix`: The naming prefix for the report files.
- `latitude` and `longitude`: The location for which weather data will be collected.
- `base_url`: The URL for calling the API.
- `variables`: Which weather variables should be requested from the API.
