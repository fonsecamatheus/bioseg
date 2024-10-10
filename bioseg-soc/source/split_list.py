def dividir_lista_em_sublistas(lista, tamanho=10):
    for i in range(0, len(lista), tamanho):
        yield lista[i:i + tamanho]