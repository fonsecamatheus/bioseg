from datetime import date

from source.config import Config
from source.http_requester import HttpRequester


class DataExtractor:
    def __init__(self, requester: HttpRequester):
        self.requester = requester
        self.anos = [ano for ano in range(2020, date.today().year+1)]

    def extrair_empresas(self):
        param = f'{{"empresa":"887992","codigo":"151534","chave":"{Config.KEY_SOC_EMPRESAS}","tipoSaida":"json","codigoEmpresa":"","codigoUnidade":"","dataInicio":"","dataFim":"","codigoGrupoProduto":"","estadoUnidade":"","codigoSubGrupo":"","diasAVencer":"60","codigoProduto":"2","statusEmpresa":"","statusUnidade":""}}'
        url = f"{Config.BASE_URL}{param}"
        return self.requester.get_data(url)
    
    def extrair_funcionarios(self, cod_empresa):
        param = f'{{"empresa":"{cod_empresa}","codigo":"138566","chave":"{Config.KEY_SOC_FUNCIONARIOS}","tipoSaida":"json","ativo":"Sim","inativo":"Sim","afastado":"Sim","pendente":"Sim","ferias":"Sim"}}'
        url = f"{Config.BASE_URL}{param}"
        return self.requester.get_data(url)

    def extrair_exames_convocacao(self, cod_empresa, codigos_funcionarios):
        param = f'{{"empresa":"887992","codigo":"149461","chave":"{Config.KEY_SOC_EXAMES_CONVOCACAO}","tipoSaida":"json","empresaTrabalho":"{cod_empresa}","funcionarios":"{codigos_funcionarios}","periodo":"12/2024","exame":"","convocarClinico":"0","nuncaRealizados":"1","periodicosNuncaRealizados":"1","selecao":"1","examesPendentes":"0","convocaPendentesPCMSO":"0"}}'
        url = f"{Config.BASE_URL}{param}"
        return self.requester.get_data(url)

    def extrair_exames_realizados(self, cod_empresa):
        for ano in self.anos:
            param = f'{{"empresa":"887992","codigo":"138569","chave":"{Config.KEY_SOC_EXAMES_REALIZADOS}","tipoSaida":"json","empresaTrabalho":"{cod_empresa}","dataInicio":"01/01/{ano}","dataFim":"31/12/{ano}"}}'
            url = f"{Config.BASE_URL}{param}"
            return self.requester.get_data(url)

    def extrair_visao_bioseg(self, cod_empresa):
        param = f'{{"empresa":"{cod_empresa}","codigo":"139629","chave":"{Config.KEY_SOC_ADICIONAIS_VISAO_BIOSEG}","tipoSaida":"json","funcionario":"1-999999999","situacaoFuncionario":"1"}}'
        url = f"{Config.BASE_URL}{param}"
        return self.requester.get_data(url)

    def extrair_esocial(self, cod_empresa):
        for ano in self.anos:
            param = f'{{"empresa":"887992","codigo":"143109","chave":"{Config.KEY_SOC_ESOCIAL}","tipoSaida":"json","empresaTrabalho":"{cod_empresa}","dataInicio":"01/01/{ano}","dataFim":"31/12/{ano}","status":"99","layout":"0","unidade":"0","ambiente":"1"}}'
            url = f"{Config.BASE_URL}{param}"
            return self.requester.get_data(url)

    def extrair_cat(self):
        for ano in self.anos:
            param = f'{{"empresa":"887992","codigo":"163423","chave":"{Config.KEY_SOC_CAT}","tipoSaida":"json","dataInicio":"01/01/{ano}","dataFim":"31/12/{ano}"}}'
            url = f'{Config.BASE_URL}{param}'
            return self.requester.get_data(url)

