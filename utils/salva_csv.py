import pandas as pd

def salvar_em_csv(dados, nome_arquivo:str):
    """
    Recebe uma lista de dicionários e salva em CSV usando pandas.
    Sempre sobrescreve o arquivo se já existir.
    """
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False, encoding="utf-8", sep=';')
    print(f"Dados exportados para {nome_arquivo}")