import pandas as pd

def transform_weather(data):
    if not data:
        return None
    
    weather = {
        "ciudad": data["name"],
        "temperatura": data["main"]["temp"],
        "humedad": data["main"]["humidity"],
        "descripcion": data["weather"][0]["description"],
    }
    
    df = pd.DataFrame([weather])
    return df

