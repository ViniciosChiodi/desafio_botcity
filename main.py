from web.fake_user.pega_fake_user import FakeDataGenerator
from web.e_commerce.acessa_ecommerce import LoginEcommerce
from web.e_commerce.coleta_dados_ecommerce import CollectData
from utils.salva_csv import salvar_em_csv

def main():
    generator = FakeDataGenerator()
    dados_contato = generator.gerar_dados()

    login = LoginEcommerce()
    login_result = login.gerar_dados()

    print("Login bem-sucedido:", login_result["success_login"])
    if not login_result["success_login"]:
        print("Erro no login:", login_result["login_error"])
    else:
        print("Login realizado com sucesso!")

        coleta_dados = CollectData(login_result["page"])
        resultado_coleta_dados = coleta_dados.collect_data()

        for item in resultado_coleta_dados["itens"]:
            print(f"{item['posicao']} - {item['nome']} | {item['descricao']} | {item['preco']}")





        # Salvar os dados de contato em um arquivo CSV
        salvar_em_csv([{"primeiro_nome": item["primeiro_nome"],
            "sobrenome": item["sobrenome"],
            "cep": item["cep"]} 
            for item in dados_contato["contato"]], "contato.csv")


        # Salvar os dados dos produtos em um arquivo CSV
        salvar_em_csv([{"posicao": item["posicao"],
            "nome": item["nome"],
            "descricao": item["descricao"],
            "preco": item["preco"]} 
            for item in resultado_coleta_dados["itens"]], "produtos.csv")




    input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
