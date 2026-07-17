import pandas as pd
import great_expectations as gx


df = pd.read_csv(
    "data/raw_sensor_data.csv"
)


context = gx.get_context()

print("GX Context Loaded Successfully")

print(df.head())