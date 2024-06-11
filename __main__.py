import pandas as pd

def json_to_excel(json_file, excel_file):
    df = pd.read_json(json_file)
    
    df.to_excel(excel_file, index=False)

json_to_excel('translated_airports.json', 'output.xlsx')