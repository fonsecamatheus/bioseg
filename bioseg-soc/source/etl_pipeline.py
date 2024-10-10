from source.data_extractor import DataExtractor
from source.http_requester import HttpRequester
from source.split_list import dividir_lista_em_sublistas


class ETL:
    def __init__(self):
        self.requester = HttpRequester()
        self.extractor = DataExtractor(self.requester)

        self.dados_empresas = []
        self.cods_empresas = []
        self.dados_funcionarios = []
        self.cods_funcionarios = []
        self.dados_exames_convocacao = []
        self.dados_exames_realizados = []
        self.dados_visao_bioseg = []
        self.dados_esocial = []
        self.dados_cat = []

    def run_pipeline_empresas(self):
        empresas = self.extractor.extrair_empresas()
        self.dados_empresas.extend(empresas)
        
        codigo_empresas = [empresa['codigoEmpresa'] for empresa in empresas]
        self.cods_empresas = list(set(codigo_empresas))

    def run_pipeline_funcionarios(self):
        for cod_empresa in self.cods_empresas:
            funcionarios = self.extractor.extrair_funcionarios(cod_empresa)
            self.dados_funcionarios.extend(funcionarios)

            codigo_funcionarios = [funcionario['CODIGO'] for funcionario in funcionarios]
            sublistas_cod_funcionarios = dividir_lista_em_sublistas(codigo_funcionarios)
            self.cods_funcionarios.append({cod_empresa: sublistas_cod_funcionarios})

    def run_pipeline_exames_convocacao(self):
        for item in self.cods_funcionarios:
            for cod_empresa, sublistas in item.items():
                for lista in sublistas:
                    exames_convocacao = self.extractor.extrair_exames_convocacao(cod_empresa, ','.join(lista))
                    self.dados_exames_convocacao.extend(exames_convocacao)

    def run_pipeline_exames_realizados(self):
        for cod_empresa in self.cods_empresas:
            exames_realizados = self.extractor.extrair_exames_realizados(cod_empresa)
            self.dados_exames_realizados.extend(exames_realizados)

    def run_pipeline_visao_bioseg(self):
        for cod_empresa in self.cods_empresas:
            visao_bioseg = self.extractor.extrair_visao_bioseg(cod_empresa)
            self.dados_visao_bioseg.extend(visao_bioseg)

    def run_pipeline_esocial(self):
        for cod_empresa in self.cods_empresas:
            esocial = self.extractor.extrair_esocial(cod_empresa)
            self.dados_esocial.extend(esocial)

    def run_pipeline_cat(self):
        cat = self.extractor.extrair_cat()
        self.dados_cat.extend(cat)
        print(cat)

