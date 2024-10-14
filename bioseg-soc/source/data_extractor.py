from datetime import date

from source.http_requester import HttpRequester
from utils.config import Config


class DataExtractor:
    def __init__(self, requester: HttpRequester):
        self.requester = requester
        self.years = [year for year in range(2020, date.today().year+1)]

    def extract_empresas(self):
        param = f'{{"empresa":"887992","codigo":"151534","chave":"{Config.KEY_SOC_EMPRESAS}","tipoSaida":"json","codigoEmpresa":"","codigoUnidade":"","dataInicio":"","dataFim":"","codigoGrupoProduto":"","estadoUnidade":"","codigoSubGrupo":"","diasAVencer":"60","codigoProduto":"2","statusEmpresa":"","statusUnidade":""}}'
        url = f"{Config.BASE_URL}{param}"
        return self.requester.get_data(url)
    
    def extract_funcionarios(self, cod_empresa):
        param = f'{{"empresa":"{cod_empresa}","codigo":"138566","chave":"{Config.KEY_SOC_FUNCIONARIOS}","tipoSaida":"json","ativo":"Sim","inativo":"Sim","afastado":"Sim","pendente":"Sim","ferias":"Sim"}}'
        url = f"{Config.BASE_URL}{param}"
        return self.requester.get_data(url)

    def extract_exames_convocacao(self, cod_empresa, cod_funcionarios):
        param = f'{{"empresa":"887992","codigo":"149461","chave":"{Config.KEY_SOC_EXAMES_CONVOCACAO}","tipoSaida":"json","empresaTrabalho":"{cod_empresa}","funcionarios":"{cod_funcionarios}","periodo":"12/2024","exame":"","convocarClinico":"0","nuncaRealizados":"1","periodicosNuncaRealizados":"1","selecao":"1","examesPendentes":"0","convocaPendentesPCMSO":"0"}}'
        url = f"{Config.BASE_URL}{param}"
        return self.requester.get_data(url)

    def extract_exames_realizados(self, cod_empresa):
        all_exames_realizados = []  
        for year in self.years:
            param = f'{{"empresa":"887992","codigo":"138569","chave":"{Config.KEY_SOC_EXAMES_REALIZADOS}","tipoSaida":"json","empresaTrabalho":"{cod_empresa}","dataInicio":"01/01/{year}","dataFim":"31/12/{year}"}}'
            url = f"{Config.BASE_URL}{param}"
            exames_realizados = self.requester.get_data(url)
            all_exames_realizados.extend(exames_realizados)  
        return all_exames_realizados  

    def extract_funcionarios_expostos(self, cod_empresa):
        param = f'{{"empresa":"{cod_empresa}","codigo":"139629","chave":"{Config.KEY_SOC_FUNCIONARIOS_EXPOSTOS}","tipoSaida":"json","funcionario":"1-999999999","situacaoFuncionario":"1"}}'
        url = f"{Config.BASE_URL}{param}"
        return self.requester.get_data(url)

    def extract_eventos_esocial(self, cod_empresa):
        all_eventos_esocial = []  
        for year in self.years:
            param = f'{{"empresa":"887992","codigo":"143109","chave":"{Config.KEY_SOC_EVENTOS_ESOCIAL}","tipoSaida":"json","empresaTrabalho":"{cod_empresa}","dataInicio":"01/01/{year}","dataFim":"31/12/{year}","status":"99","layout":"0","unidade":"0","ambiente":"1"}}'
            url = f"{Config.BASE_URL}{param}"
            eventos_esocial = self.requester.get_data(url)
            all_eventos_esocial.extend(eventos_esocial) 
        return all_eventos_esocial  

    def extract_cats(self):
        all_cats = [] 
        for year in self.years:
            param = f'{{"empresa":"887992","codigo":"163423","chave":"{Config.KEY_SOC_CAT}","tipoSaida":"json","dataInicio":"01/01/{year}","dataFim":"31/12/{year}"}}'
            url = f'{Config.BASE_URL}{param}'
            cats = self.requester.get_data(url)
            all_cats.extend(cats)  
        return all_cats 
