import pandas as pd


class DataLoader:
    def __init__(self):
        pass

    def load_to_excel(self, df: pd.DataFrame, file_path: str, sheet_name: str = 'Sheet1'):
        try:
            df.to_excel(file_path, sheet_name=sheet_name, index=False)
            print(f'Dados salvos com sucesso em {file_path}')
        except Exception as e:
            print(f'Erro ao salvar os dados em Excel: {e}')