from web.pega_fake_user import FakeDataGenerator

def main():
    generator = FakeDataGenerator()
    dados = generator.gerar_dados()

    print("Primeiro nome:", dados["primeiro_nome"])
    print("Sobrenome:", dados["sobrenome"])
    print("CEP:", dados["cep"])

if __name__ == "__main__":
    main()
