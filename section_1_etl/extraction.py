import pandas as pd
import os

def extract_from_csv(file_path):
    """
    Leer el dataset original y exportarlo al Parquet.
    """
    if not os.path.exists(file_path):
        print(f"Error: No se encontró el archivo en {file_path}")
        return None
    df = pd.read_csv(file_path)
    output_path = "data/data_extraida.parquet"
    df.to_parquet(output_path, engine='pyarrow')
    print(f"Extracción completada con éxito: {output_path}")
    return output_path