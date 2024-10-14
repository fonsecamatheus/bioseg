import pandas as pandas


class DataTransformer:
    def __init__(self):
        pass

    def transform_empresas(self, empresas_data):
        empresas_df = pandas.DataFrame(empresas_data)
        return empresas_df

    def transform_funcionarios(self, funcionarios_data):
        funcionarios_df = pandas.DataFrame(funcionarios_data)
        return funcionarios_df

    def transform_exames_convocacao(self, exames_convocacao_data):
        exames_convocacao_df = pandas.DataFrame(exames_convocacao_data)
        return exames_convocacao_df

    def transform_exames_realizados(self, exames_realizados_data):
        exames_realizados_df = pandas.DataFrame(exames_realizados_data)
        return exames_realizados_df

    def transform_funcionarios_expostos(self, funcionarios_expostos_data):
        funcionarios_expostos_df = pandas.DataFrame(funcionarios_expostos_data)
        return funcionarios_expostos_df

    def transform_eventos_esocial(self, eventos_esocial_data):
        eventos_esocial_df = pandas.DataFrame(eventos_esocial_data)
        return eventos_esocial_df

    def transform_cats(self, cats_data):
        cats_df = pandas.DataFrame(cats_data)
        return cats_df
