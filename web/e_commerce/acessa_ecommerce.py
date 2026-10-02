from playwright.sync_api import sync_playwright

import os
from dotenv import load_dotenv
# Carrega variáveis do arquivo .env
load_dotenv()
# Acessa as variáveis
USER_ECOMMERCE = os.getenv("USER_ECOMMERCE")
PASSWORD_ECOMMERCE = os.getenv("PASSWORD_ECOMMERCE")


class LoginEcommerce:
    def __init__(self, chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        # Caminho do executável do Chrome
        self.chrome_path = chrome_path

    def gerar_dados(self):
        p =  sync_playwright().start()
        # Abre o navegador
        browser = p.chromium.launch(
            headless=False,  # Executa em modo invisível
            executable_path=self.chrome_path
        )

        page = browser.new_page()

        # Acessa o site
        page.goto("https://www.saucedemo.com/")

        # -- Preenche User --
        page.fill("#user-name", USER_ECOMMERCE)

        # -- Preenche Password --
        page.fill("#password", PASSWORD_ECOMMERCE)

        # Clica no botão de login
        page.click("#login-button")

        # Espera o elemento que só aparece após login
        try:
            page.wait_for_selector(".app_logo")
            success_login = True

            # Retorna os dados
            return {
                "success_login": success_login,
                "page": page
            }

        except Exception as e:
            success_login = False
            retorn_login_error = str(e)

            # Fecha navegador
            browser.close()

            # Retorna os dados
            return {
                "success_login": success_login,
                "login_error": retorn_login_error,
                "page": page
            }


