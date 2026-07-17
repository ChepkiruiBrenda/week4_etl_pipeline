# Week 4 ETL Pipeline

## Overview

This project demonstrates a production-style ETL (Extract, Transform, Load) pipeline built in Python.

The pipeline:

- Extracts raw warehouse sensor data from a CSV file.
- Cleans and transforms the data.
- Validates data quality using Great Expectations.
- Loads validated data into a SQLite database.
- Records execution logs for monitoring.

---

## Project Structure

```
week4_etl_pipeline/
│
├── data/
│   ├── raw_sensor_data.csv
│   └── ops_database.db
│
├── logs/
│   └── pipeline.log
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── run_pipeline.py
├── validate_data.py
└── automation_proof.png
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd week4_etl_pipeline
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file from `.env.example`

Example

```
DB_PATH=data/ops_database.db
LOG_FILE=logs/pipeline.log
PRESSURE_MIN=0
PRESSURE_MAX=200
TEMP_MAX=100
```

---

## Running the Pipeline

```bash
python run_pipeline.py
```

---

## Features

- Modular ETL architecture
- Data validation with Great Expectations
- SQLite data loading
- Idempotent loading
- Logging
- Environment variable configuration

---

## Author

Brenda Chepkirui
PLP Academy – Week 4 Assignment