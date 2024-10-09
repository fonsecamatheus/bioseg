from source.execute_query import execute_query
from source.save_to_excel import save_to_excel


def pipeline(query, excel_file):
    df = execute_query(query)
    
    if df is not None and not df.empty:
        save_to_excel(df, excel_file)
    else:
        print('Nenhum dado foi retornado ou o dataframe está vazio')