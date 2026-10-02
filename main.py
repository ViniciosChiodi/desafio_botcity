from utils.logs import setup_logger
import logging

from web import coleta_dados
from desktop import preenche_dados


def main():
    try:
        setup_logger()

        """
        Automação foi estruturada em três partes:
        
        1. Coleta de dados do e-commerce e de cliente novo
        2. Preenchimento de dados de contato no sistema Fakturama
        3. Preenchimento de dados de produtos no sistema Fakturama
        """

        logging.info("Iniciando Automação Fakturama")

        # -- Coleta de dados --
        coleta_dados.collect_data()

        # -- Preenchimento de dados --
        preenche_dados.preenche_dados_contato()

        preenche_dados.preenche_produtos()

        logging.info("Automação Fakturama concluída com sucesso!")
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")



if __name__ == "__main__":
    main()
