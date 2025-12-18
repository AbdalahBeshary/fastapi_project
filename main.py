from fastapi import  FastAPI
import pandas as pd


app=FastAPI()
URL="https://docs.google.com/spreadsheets/d/1XrZvN4yz9DTirFLh0MdGZ3pIZmfzxsD8oVqgeSXvIDE/export?format=csv"
@app.get('/student')
def get_google_sheet_data():
    df=pd.read_csv(URL)

    

    return df.to_dict(orient="records")
