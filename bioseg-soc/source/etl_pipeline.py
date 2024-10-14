from source.data_extractor import DataExtractor
from source.data_loader import DataLoader
from source.data_transform import DataTransformer
from source.http_requester import HttpRequester
from utils.split_list_into_sublists import split_list_into_sublists


class ETL:
    def __init__(self):
        self.requester = HttpRequester()
        self.extractor = DataExtractor(self.requester)
        self.transformer = DataTransformer()
        self.loader = DataLoader()

        self.empresas_data = []
        self.cods_empresas = []
        self.funcionarios_data = []
        self.cods_funcionarios = []
        self.exames_convocacao_data = []
        self.exames_realizados_data = []
        self.funcionarios_expostos_data = []
        self.eventos_esocial_data = []
        self.cats_data = []

    def run_pipeline_empresas(self):
        empresas = self.extractor.extract_empresas()
        self.empresas_data.extend(empresas)
        
        codigo_empresas = [empresa['codigoEmpresa'] for empresa in empresas]
        self.cods_empresas = list(set(codigo_empresas))

        empresas_df = self.transformer.transform_empresas(self.empresas_data)
        self.loader.load_to_excel(empresas_df, file_path='data/EMPRESAS.xlsx')

    def run_pipeline_funcionarios(self):
        for cod_empresa in self.cods_empresas:
            funcionarios = self.extractor.extract_funcionarios(cod_empresa)
            self.funcionarios_data.extend(funcionarios)

            codigo_funcionarios = [funcionario['CODIGO'] for funcionario in funcionarios]
            sublistas_cod_funcionarios = split_list_into_sublists(codigo_funcionarios)
            self.cods_funcionarios.append({cod_empresa: sublistas_cod_funcionarios})

        funcionarios_df = self.transformer.transform_funcionarios(self.funcionarios_data)
        self.loader.load_to_excel(funcionarios_df, file_path='data/FUNCIONÁRIOS.xlsx')

    def run_pipeline_exames_convocacao(self):
        for item in self.cods_funcionarios:
            for cod_empresa, sublistas in item.items():
                for lista in sublistas:
                    exames_convocacao = self.extractor.extract_exames_convocacao(cod_empresa, ','.join(lista))
                    self.exames_convocacao_data.extend(exames_convocacao)
        
        exames_convocacao_df = self.transformer.transform_exames_convocacao(self.exames_convocacao_data)
        self.loader.load_to_excel(exames_convocacao_df, file_path='data/CONVOCAÇÃO DE EXAMES.xlsx')

    def run_pipeline_exames_realizados(self):
        for cod_empresa in self.cods_empresas:
            exames_realizados = self.extractor.extract_exames_realizados(cod_empresa)
            self.exames_realizados_data.extend(exames_realizados)
        
        exames_realizados_df = self.transformer.transform_exames_realizados(self.exames_realizados_data)
        self.loader.load_to_excel(exames_realizados_df, file_path='data/EXAMES REALIZADOS.xlsx')

    def run_pipeline_funcionarios_expostos(self):
        for cod_empresa in self.cods_empresas:
            funcionarios_expostos = self.extractor.extract_funcionarios_expostos(cod_empresa)
            self.funcionarios_expostos_data.extend(funcionarios_expostos)
    
        funcionarios_expostos_df = self.transformer.transform_funcionarios_expostos(self.funcionarios_expostos_data)
        self.loader.load_to_excel(funcionarios_expostos_df, file_path='data/FUNCIONÁRIOS EXPOSTOS.xlsx')

    def run_pipeline_eventos_esocial(self):
        for cod_empresa in self.cods_empresas:
            eventos_esocial = self.extractor.extract_eventos_esocial(cod_empresa)
            self.eventos_esocial_data.extend(eventos_esocial)
    
        eventos_esocial_df = self.transformer.transform_eventos_esocial(self.eventos_esocial_data)
        self.loader.load_to_excel(eventos_esocial_df, file_path='data/EVENTOS ESOCIAL.xlsx')

    def run_pipeline_cats(self):
        cats = self.extractor.extract_cats()
        self.cats_data.extend(cats)

        cats_df = self.transformer.transform_cats(self.cats_data)
        self.loader.load_to_excel(cats_df, file_path='data/CATs.xlsx')

