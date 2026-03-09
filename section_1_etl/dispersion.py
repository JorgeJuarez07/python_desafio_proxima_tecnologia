import pandas as pd

def disperse_data(df, engine):
    """
    Separa la información en 'companies' y 'charges' y carga en la DB.
    """
    companies_df = df[['company_id', 'name']].drop_duplicates()
    companies_df.columns = ['id', 'name']
    charges_df = df[['id', 'name', 'company_id', 'amount', 'status', 'created_at', 'paid_at']].copy()
    charges_df.columns = ['id', 'company_name', 'company_id', 'amount', 'status', 'created_at', 'updated_at']
    
    try:
        companies_df.to_sql('companies', engine, if_exists='append', index=False)
        charges_df.to_sql('charges', engine, if_exists='append', index=False)
        print("Dispersión exitosa: Datos cargados en Docker.")
    except Exception as e:
        print(f"Error cargando a la base de datos: {e}")