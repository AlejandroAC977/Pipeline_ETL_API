from extract import get_weather
from transform import transform_weather
from load import save_to_csv

def run_pipe():
    data= get_weather()
    df=transform_weather(data)

    if df is not None:
        save_to_csv(df)
        print("pipeline ejecutada")

if __name__ == "__main__":
    run_pipe()