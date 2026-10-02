import logging

from web.fake_user.pega_fake_user import FakeDataGenerator
from web.e_commerce.acessa_ecommerce import LoginEcommerce
from web.e_commerce.coleta_dados_ecommerce import CollectData
from utils.salva_csv import salvar_em_csv


def collect_data():
    logging.info("Iniciando coleta de dados do e-commerce e geração de dados de contato.")

    generator = FakeDataGenerator()
    dados_contato = generator.gerar_dados()
    logging.info("Dados de contato gerados com sucesso.")

    login = LoginEcommerce()
    login_result = login.gerar_dados()
    

    if not login_result["success_login"]:
        logging.error("Erro no login: %s", login_result["login_error"])
    else:
        logging.info("Login no e-commerce realizado com sucesso.")

        coleta_dados = CollectData(login_result["page"])
        resultado_coleta_dados = coleta_dados.collect_data()
        logging.info("Coleta de dados do e-commerce concluída com sucesso.")

        # Salvar os dados de contato em um arquivo CSV
        salvar_em_csv([{"primeiro_nome": item["primeiro_nome"],
            "sobrenome": item["sobrenome"],
            "cep": item["cep"]} 
            for item in dados_contato["contato"]], "contato.csv")
        logging.info("Dados de contato salvos em contato.csv")

        # Salvar os dados dos produtos em um arquivo CSV
        salvar_em_csv([{"posicao": item["posicao"],
            "nome_produto": item["nome_produto"],
            "descricao": item["descricao"],
            "preco": item["preco"]} 
            for item in resultado_coleta_dados["itens"]], "produtos.csv")
        logging.info("Dados dos produtos salvos em produtos.csv")