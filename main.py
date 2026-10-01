from web.pega_fake_user import FakeDataGenerator
from web.acessa_souce import LoginEcommerce

def main():
    generator = FakeDataGenerator()
    dados = generator.gerar_dados()

    login = LoginEcommerce()
    login_result = login.gerar_dados()

    print("Primeiro nome:", dados["primeiro_nome"])
    print("Sobrenome:", dados["sobrenome"])
    print("CEP:", dados["cep"])

    print("Login bem-sucedido:", login_result["success_login"])
    if not login_result["success_login"]:
        print("Erro no login:", login_result["login_error"])



    input("Pressione Enter para continuar...")

    print("Primeiro nome:", dados["primeiro_nome"])
    print("Sobrenome:", dados["sobrenome"])
    print("CEP:", dados["cep"])

if __name__ == "__main__":
    main()
