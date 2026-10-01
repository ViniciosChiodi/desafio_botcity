from playwright.sync_api import sync_playwright

class FakeDataGenerator:
    def __init__(self, chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        # Caminho do executável do Chrome
        self.chrome_path = chrome_path

    def gerar_dados(self):
        with sync_playwright() as p:
            # Abre o navegador
            browser = p.chromium.launch(
                headless=True,  # Executa em modo invisível
                executable_path=self.chrome_path
            )

            page = browser.new_page()

            # Acessa o site
            page.goto("https://www.fakenamegenerator.com/gen-random-br-br.php")

            # -- Pega Nome --
            # Espera o elemento aparecer
            page.wait_for_selector("div.address h3")
            nome_completo = page.text_content("div.address h3")

            # Separar nome e sobrenome:
            lista_nome_completo = nome_completo.split()
            primeiro_nome = lista_nome_completo[0]
            sobrenome = " ".join(lista_nome_completo[1:])

            # -- Pega CEP --
            # Pega o HTML do bloco de endereço
            endereco_html = page.inner_html("div.adr")

            # Divide pelo <br>
            partes = [parte.strip() for parte in endereco_html.split("<br>") if parte.strip()]
            cep = partes[2]



            # Fecha navegador
            browser.close()

            # Retorna os dados como dicionário
            return {
                "primeiro_nome": primeiro_nome,
                "sobrenome": sobrenome,
                "cep": cep
            }
