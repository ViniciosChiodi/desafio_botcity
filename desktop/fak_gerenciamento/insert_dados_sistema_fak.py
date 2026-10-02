import logging
import time

import pyautogui
from desktop.fak_gerenciamento.opera_sistema_fak import OperaFakturama

class InsertDadosContactSistemaFak:
    """
    Código feito com mapeamento de campo através de imagens,
    se atentar que os campos podem mudar de posição, então em certo casos pode ser
    necessário atualizar as imagens de referência.  
    """
    def __init__(self):
        self.fakturama = OperaFakturama()

    def novo_contato(self):
        time.sleep(2)  # Aguarda 2 segundos
        botao_new_contact = pyautogui.locateOnScreen(r"desktop\imagens_fak\new_contact.png", confidence=0.6)
        if botao_new_contact:
            pyautogui.click(botao_new_contact)
            logging.info("Botão de novo contato encontrado e clicado!")
        else:
            logging.error("Botão de novo contato não encontrado na tela.")

    def preenche_dados_contato(self,first_name, last_name, cep_init, cep_end):
        time.sleep(2)  # Aguarda 2 segundos    
        while True:
            campo_nome = pyautogui.locateOnScreen(r"desktop\imagens_fak\label_name.png", confidence=0.6)
            if campo_nome:
                x, y = pyautogui.center(campo_nome)
                pyautogui.click(x + 150, y)  # desloca 150px à direita
                break
            time.sleep(1)

        pyautogui.write(first_name)
        pyautogui.press("tab")  # pula para o próximo campo
        pyautogui.write(last_name)

        time.sleep(2)  # Aguarda 2 segundos
        while True:
            campo_cep = pyautogui.locateOnScreen(r"desktop\imagens_fak\label_cep.png", confidence=0.6)
            if campo_cep:
                x, y = pyautogui.center(campo_cep)
                pyautogui.click(x + 50, y)  # desloca 50px à direita
                break
            time.sleep(1)

        pyautogui.write(cep_init)
        pyautogui.press("tab")  # pula para o próximo campo
        pyautogui.write(cep_end)

    def novo_produto(self):
        time.sleep(2)  # Aguarda 2 segundos
        botao_new_product = pyautogui.locateOnScreen(r"desktop\imagens_fak\new_product.png", confidence=0.6)
        if botao_new_product:
            pyautogui.click(botao_new_product)
            logging.info("Botão de novo produto encontrado e clicado!")
        else:
            logging.error("Botão de novo produto não encontrado na tela.")

    def preenche_dados_produto(self, position, product_name, description, price):
        time.sleep(2)  # Aguarda 2 segundos    
        while True:
            item_number = pyautogui.locateOnScreen(r"desktop\imagens_fak\item_number.png", confidence=0.9)
            if item_number:
                x, y = pyautogui.center(item_number)
                pyautogui.click(x + 100, y)  # desloca 100px à direita
                logging.info("Item número do produto encontrado na tela!")
                break
            else:
                logging.warning("Item número do produto não encontrado na tela. Tentando novamente...")
            time.sleep(1)

        pyautogui.write(position)

        time.sleep(2)  # Aguarda 2 segundos
        while True:
            item_name = pyautogui.locateOnScreen(r"desktop\imagens_fak\product_name.png", confidence=0.9)
            if item_name:
                logging.info("Item nome do produto encontrado na tela!")
                x, y = pyautogui.center(item_name)
                pyautogui.click(x + 100, y)  # desloca 100px à direita
                break
            else:
                logging.warning("Item nome do produto não encontrado na tela. Tentando novamente...")
            time.sleep(1)

        pyautogui.write(product_name)

        time.sleep(2)  # Aguarda 2 segundos

        # Localiza todas as imagens "description.png" na tela
        all_description_images = list(pyautogui.locateAllOnScreen(r"desktop\imagens_fak\description.png", confidence=0.6))

        if len(all_description_images) >= 2:
            # pega a segunda ocorrência
            item_description = all_description_images[1]
            x, y = pyautogui.center(item_description)
            pyautogui.click(x + 100, y)  # ajuste deslocamento conforme necessário
            time.sleep(1)

        pyautogui.write(description)

        time.sleep(2)  # Aguarda 2 segundos
        while True:
            item_price = pyautogui.locateOnScreen(r"desktop\imagens_fak\price.png", confidence=0.9)
            if item_price:
                x, y = pyautogui.center(item_price)
                pyautogui.click(x + 100, y)  # desloca 100px à direita
                break
            time.sleep(1)

        pyautogui.write(str(price))

    def salvar_insert(self):
        time.sleep(2)  # Aguarda 2 segundos
        botao_save = pyautogui.locateOnScreen(r"desktop\imagens_fak\save_button.png", confidence=0.8)
        if botao_save:
            pyautogui.click(botao_save)
            logging.info("Botão de salvar encontrado e clicado!")
        else:
            logging.error("Botão de salvar não encontrado na tela.")