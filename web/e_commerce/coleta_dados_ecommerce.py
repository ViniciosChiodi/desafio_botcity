from playwright.sync_api import sync_playwright

class CollectData:
    def __init__(self, page):
        self.page = page
    def collect_data(self):
        # Espera o container aparecer
        self.page.wait_for_selector("#inventory_container")

        # Seleciona todos os itens
        itens = self.page.query_selector_all(".inventory_item")

        dados = []
        for posicao, item in enumerate(itens, start=1):
            # Nome do produto
            nome = item.query_selector(".inventory_item_name").text_content()

            # Descrição
            descricao = item.query_selector(".inventory_item_desc").text_content()

            # Preço
            preco = item.query_selector(".inventory_item_price").text_content()

            # Adiciona todas as informações no dicionário
            dados.append({
                "posicao": posicao,
                "nome_produto": nome.strip(),
                "descricao": descricao.strip(),
                "preco": preco.strip().replace("R$", "").replace(".", ",")
            })

        self.page.close()  # Fecha a página após coletar os dados

        return {"itens": dados}