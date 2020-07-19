import scrapy


class QuotesSpider(scrapy.Spider):
    name = "citacoes4"
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'texto': quote.css('span.text::text').extract_first(),
                'autor': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        pagina = response.url.split("/")[-2]
        nome_arquivo = f'citacoes-{pagina}.html'
        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)