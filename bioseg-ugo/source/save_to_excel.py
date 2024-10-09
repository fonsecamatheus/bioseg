def save_to_excel(df, excel_file):
    try:
        df.to_excel(excel_file, index=False, engine='openpyxl')
        print(f'Dados salvos no caminho {excel_file}')
    except Exception as e:
        print(f'Erro ao salvar: {e}')