import os
import pandas


sheets_to_exclude = ['Resumo Grafico', 'Resumo Plano de Ação', 'BASE', 'Planilha1']

columns_to_extracted = ['Data Início', 'Setor', 'O que Fazer', 'Quem Fará', 'Fase', 
                        'Ano', 'Prazo ', 'Situação', 'Conclusão', 'Meta', 'Aprov. Final']

#Função para carregar planilhas específicas, filtrar e criar colunas, tratar datas
def load_sheets(file_path, area_name):
    dataframes = []

    try:
        xls = pandas.ExcelFile(file_path)
        for sheet in xls.sheet_names:
            if sheet not in sheets_to_exclude:
                df = pandas.read_excel(xls, sheet_name=sheet, header=7)

                if 'Situação' in df.columns:
                    end_index = df[df['Situação'] == 'Total Ações'].index
                    if not end_index.empty:
                        end_index = end_index[0]
                        df = df.iloc[:end_index]

                df = df.dropna(how='all')

                filtered_df = df[columns_to_extracted] if set(columns_to_extracted).issubset(df.columns) else pandas.DataFrame()
                
                if not filtered_df.empty:
                    for column in ['Data Início', 'Prazo ', 'Conclusão']:
                        if column in filtered_df.columns:
                            filtered_df[column] = pandas.to_datetime(filtered_df[column], errors='coerce').dt.strftime('%d/%m/%Y')
                    filtered_df['Área'] = area_name
                    filtered_df['Iniciativa'] = sheet
                    dataframes.append(filtered_df)
                    print(f'Planilha "{sheet}" carregada com sucesso')

    except Exception as e:
        print(f'Erro ao carregar o arquivo {file_path}: {e}')
    return dataframes

#Função para processar todos os arquivos da pasta e concatenar dataframes
def process_folder(folder_path):
    all_dataframes = []
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.xls', '.xlsm')):
            file_path = os.path.join(folder_path, file_name)
            area_name = file_name.split('-')[-1].replace('.xls', '').replace('.xlsm', '').strip()
            dataframes = load_sheets(file_path, area_name)
            all_dataframes.extend(dataframes)

    if all_dataframes:
        df_concatenado = pandas.concat(all_dataframes, ignore_index=True)
        print('Dataframes concatenados com sucesso')
        return df_concatenado
    else:
        print('Nenhum dataframe foi carregado')
        return pandas.DataFrame()  


if __name__ == '__main__':
    folder_path = r'H:\REUNIÃO GERENCIAL - REGER\FORMULÁRIOS\MATRIZ PLANO DE AÇÃO'
    concatened_df = process_folder(folder_path)
    concatened_df.to_excel(r'\PLANO DE AÇÃO GERENCIAL.xlsx', index=False)
