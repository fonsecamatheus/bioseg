from playwright.sync_api import sync_playwright

from source.login import login
from source.pagina271 import pagina271
from source.pagina662 import pagina662
from source.pulando_avisos import pulando_avisos
from source.requisitando_empresas import (requisitando_empresas,
                                          tratamento_duplicadas)


def main(playwright):
    dados_empresas = requisitando_empresas()
    dict_empresas = tratamento_duplicadas(dados_empresas)
    dict_empresas = {
        '1159700': 'PREFEITURA MUNICIPAL DE CUIABA',
        '1346087': 'LIMPURB EMPRESA CUIABANA DE LIMPEZA URBANA',
        '1346052': 'PRODECAP PROGRESSO E DESENVOLVIMENTO DA CAPITAL SA',
        '1543261': 'MUNICIPIO DE ALTO GARCAS',
        '1489132': 'MUNICIPIO DE MATUPA',
        '1532501': 'MUNICIPIO DE SALTO DO CEU',
        '1234142': 'MUNICIPIO DE SINOP'
    }

    navegador = playwright.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    login(pagina)
    pulando_avisos(pagina)
    dict_empresas = pagina662(pagina, dict_empresas)
    pagina271(pagina, dict_empresas)


with sync_playwright() as playwright:
    main(playwright)