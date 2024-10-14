from source.etl_pipeline import ETL

if __name__ == '__main__':
    etl = ETL()
    etl.run_pipeline_empresas()
    etl.run_pipeline_funcionarios()
    etl.run_pipeline_exames_convocacao()
    etl.run_pipeline_exames_realizados()
    etl.run_pipeline_funcionarios_expostos()
    etl.run_pipeline_eventos_esocial()
    etl.run_pipeline_cats()