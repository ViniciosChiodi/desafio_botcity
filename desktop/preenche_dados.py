import csv
import logging
import time

from desktop.fak_gerenciamento.insert_dados_sistema_fak import InsertDadosContactSistemaFak
from desktop.fak_gerenciamento.opera_sistema_fak import OperaFakturama

def preenche_dados_contato():
    logging.info("Iniciando preenchimento de dados de contato no sistema Fakturama")
    fakturama = OperaFakturama()
    if fakturama.fakturama_execucao():
    
        insert_dados = InsertDadosContactSistemaFak()

        with open("csvs\\contato.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")

            for row in reader:
                first_name = row["primeiro_nome"]
                last_name = row["sobrenome"]
                cep = row["cep"]

                cep_init, cep_end = cep.split("-")

                logging.info(f"Preenchendo dados de contato")
                insert_dados.novo_contato()
                insert_dados.preenche_dados_contato(first_name, last_name, cep_init, cep_end)
                insert_dados.salvar_insert()
                logging.info(f"Dados de contato salvos com sucesso: {first_name} {last_name}")

    else:
        logging.error("Fakturama não está em execução. Por favor, abra o Fakturama e tente novamente.")
        return False

def preenche_produtos():
    logging.info("Iniciando preenchimento de dados de produtos no sistema Fakturama")
    fakturama = OperaFakturama()
    if fakturama.fakturama_execucao():
    
        insert_dados = InsertDadosContactSistemaFak()

        with open("csvs\\produtos.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")

            for row in reader:
                numero = row["posicao"]
                nome_produto = row["nome_produto"]
                descricao = row["descricao"]
                preco = row["preco"]

                logging.info("Preenchendo dados de produto")
                insert_dados.novo_produto()
                insert_dados.preenche_dados_produto(position=numero, product_name=nome_produto, description=descricao, price=preco)

                logging.info(f"Dados de produto salvos com sucesso: {nome_produto}")
                time.sleep(2)  # Aguarda 2 segundos antes de prosseguir
                insert_dados.salvar_insert()

        fakturama.fechar_fakturama()
    else:
        logging.error("Fakturama não está em execução. Por favor, abra o Fakturama e tente novamente.")
        return False