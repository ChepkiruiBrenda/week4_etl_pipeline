import os
import logging
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

DB_PATH = os.getenv("DB_PATH", "data/ops_database.db")
LOG_FILE = os.getenv("LOG_FILE", "logs/pipeline.log")

PRESSURE_MIN = float(os.getenv("PRESSURE_MIN", 0))
PRESSURE_MAX = float(os.getenv("PRESSURE_MAX", 200))
TEMP_MAX = float(os.getenv("TEMP_MAX", 100))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
#Extract Phase
def extract_data():
    """Extract data from CSV."""

    logging.info("Starting Extraction Phase...")

    try:
        df = pd.read_csv("data/raw_sensor_data.csv")

        logging.info(f"Extracted {len(df)} rows.")

        return df

    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        raise

#Transform phase
def transform_data(df):
    """
    Clean and validate the extracted data.
    """

    logging.info("Starting Transformation Phase...")

    try:
        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove rows with missing values
        df = df.dropna()

        # Convert timestamp column
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Keep only valid pressure readings
        df = df[
            (df["pressure_psi"] > PRESSURE_MIN) &
            (df["pressure_psi"] <= PRESSURE_MAX)
        ]

        # Keep only acceptable temperatures
        df = df[df["temperature"] <= TEMP_MAX]

        logging.info(f"Transformation complete. {len(df)} valid rows remaining.")

        return df

    except Exception as e:
        logging.error(f"Transformation failed: {e}")
        raise

# Pipeline Execution
if __name__ == "__main__":

    logging.info("========== Pipeline Started ==========")

    raw_data = extract_data()

    clean_data = transform_data(raw_data)

    print("\nCleaned Data:\n")
    print(clean_data)

    logging.info("========== Extract & Transform Completed ==========")