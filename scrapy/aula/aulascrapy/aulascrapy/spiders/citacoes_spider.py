import scrapy

"""
Este Módulo possui uma classe para realização de crawler no site quotes.toscrape.com
"""
class SpiderCitacoes(scrapy.Spider):
    """
    Classe para realização de crawler no site quotes.toscrape.com
    """
    # Definindo o nome do Spider
    name = "citacoes"

    def start_requests(self):
        """
        Método que realizará o agendamento das requisições
        :return: Lista de Request
        """
        # Criando uma lista de endereços que serão acessados

        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        # Realizando um loop na lista de endereços
        # e retornando um objeto Request para cada endereço acessado
        # os parâmetros de scrapy.Request são "url" que é o endereço
        # e "callback", que é a função que será chamada para tratar a requisição
        # Aqui o scrapy vai agendando as requisições
        # O yield retorna um generator o chamador da função
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, resposta):
        """
        Método que realiza o tratamento da resposta das requisições
        :param resposta: Parâmetro que receberá a resposta de scrapy.Request
        """
        # Quebrando a URL com base no caractere "/" teremos o resultado abaixo
        # ['http:', '', 'quotes.toscrape.com', 'page', '1', '']
        # Para pegar o número da página temos que pegar o penúltimo elemento da lista fatiando com "-2"
        # Assim, página será "1" e depois "2"
        pagina = resposta.url.split("/")[-2]
        # Definindo o nome de arquivo como "citacoes-1.html" e depois "citacoes-2.html"
        nome_arquivo = f'citacoes-{pagina}.html'
        # Abrindo o arquivo criado para escrita e gravando o conteúdo do elemento body
        # da resposta (Request)
        with open(nome_arquivo, 'wb') as f:
            f.write(resposta.body)

        # Aqui estamos logando a informação "Arquivo salvo", seguido do nome do arquivo
        self.log(f'Arquivo salvo {nome_arquivo}')