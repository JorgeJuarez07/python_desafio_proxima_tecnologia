import pandas as pd

def transform_data(parquet_path):
    """
    Limpia y normaliza los datos del parquet antes de cargarlos en la DB.
    """
    df = pd.read_parquet(parquet_path)
    df = df.dropna(subset=['id', 'company_id'])
    df['created_at'] = pd.to_datetime(df['created_at'], format='ISO8601', errors='coerce')
    df['paid_at'] = pd.to_datetime(df['paid_at'], format='ISO8601', errors='coerce')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    return df