from utils.logs import setup_logger
import logging

from web import coleta_dados
from desktop import preenche_dados


def main():
    # setup_logger()
    # logging.info("Iniciando o script principal...")

    # coleta_dados.collect_data()

    # preenche_dados.preenche_dados_contato()
    preenche_dados.preenche_produtos()


    input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
