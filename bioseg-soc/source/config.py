import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv('BASE_URL')
    KEY_SOC_EMPRESAS = os.getenv('KEY_SOC_EMPRESAS')
    KEY_SOC_FUNCIONARIOS = os.getenv('KEY_SOC_FUNCIONARIOS')
    KEY_SOC_ADICIONAIS_VISAO_BIOSEG = os.getenv('KEY_SOC_ADICIONAIS_VISAO_BIOSEG')
    KEY_SOC_EXAMES_CONVOCACAO = os.getenv('KEY_SOC_EXAMES_CONVOCACAO')
    KEY_SOC_ESOCIAL = os.getenv('KEY_SOC_ESOCIAL')
    KEY_SOC_EXAMES_REALIZADOS = os.getenv('KEY_SOC_EXAMES_REALIZADOS')
    KEY_SOC_LOG_ACOES=os.getenv('KEY_SOC_LOG_ACOES')
    KEY_SOC_COMBO_PROGS=os.getenv('KEY_SOC_COMBO_PROGS')
    KEY_SOC_CAT = os.getenv('KEY_SOC_CAT')
