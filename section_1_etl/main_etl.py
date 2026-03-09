import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from extraction import extract_from_csv
from transformation import transform_data
from dispersion import disperse_data

load_dotenv()

DB_USER = os.getenv("DATABASE_USER")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def run_pipeline():
    raw_csv = "data/data_prueba_tecnica.csv"
    parquet_file = extract_from_csv(raw_csv)
    
    if parquet_file:
        df_clean = transform_data(parquet_file)
        disperse_data(df_clean, engine)
        print("Proceso finalizado con exito.")

if __name__ == "__main__":
    run_pipeline()