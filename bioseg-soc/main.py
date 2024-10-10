from source.etl_pipeline import ETL


if __name__ == '__main__':
    etl = ETL()
    #etl.run_pipeline_empresas()
    #etl.run_pipeline_funcionarios()
    #etl.run_pipeline_exames_convocacao()
    #etl.run_pipeline_exames_realizados()
    #etl.run_pipeline_visao_bioseg()
    #etl.run_pipeline_esocial()
    etl.run_pipeline_cat()