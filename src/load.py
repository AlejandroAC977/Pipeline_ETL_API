import pandas as pd
import os

"""
def save_to_csv(df):
    file_path ="data"

    if os.path.exists(file_path):
        df.to_csv(os.path.join(file_path, "weather_data.csv"), mode="a", header=False, index=False)
    else:
        df.to_csv(file_path, index=False) 
"""

"""     
def save_to_csv(df):
    folder_path = "data"
    file_name = "weather_data.csv"
    full_path = os.path.join(folder_path, file_name)

    # Crear la carpeta si no existe
    os.makedirs(folder_path, exist_ok=True)

    # Si el archivo ya existe → append sin header
    if os.path.exists(full_path):
        df.to_csv(full_path, mode="a", header=False, index=False)
    else:
        df.to_csv(full_path, index=False)
"""

def save_to_csv(df):
    base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    folder_path=os.path.join(base_dir, "data")
    file_path=os.path.join(folder_path, "weather_data.csv")

    if os.path.exists(file_path):
        df.to_csv(file_path, mode="a", header=False, index=False)
    else:
        df.to_csv(file_path, index=False)