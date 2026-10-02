from pathlib import Path

import pandas as pd

def salvar_em_csv(dados, nome_arquivo:str):
    """
    Recebe uma lista de dicionários e salva em CSV usando pandas.
    Sempre sobrescreve o arquivo se já existir.
    """
    df = pd.DataFrame(dados)
    diretorio_csv = Path(__file__).resolve().parent.parent / "csvs"
    diretorio_csv.mkdir(parents=True, exist_ok=True)
    df.to_csv(diretorio_csv / nome_arquivo, index=False, encoding="utf-8", sep=';')