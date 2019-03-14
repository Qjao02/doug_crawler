import scrapy

class BoletimSpider(scrapy.Spider):
    name = 'boletim'

    def start_requests(self):
        urls = []

        for i in range (1,91):
            urls.append('https://ufsj.edu.br/ascom/boletim{0:03}.php'.format(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, encoding='utf-8')

    def parse(self, response):
        boletim =  {
            'boletim-titulo' :  response.xpath('//p[@class="titulo-int2"]/text()').get(),
            'noticia-titulo' :  response.xpath('//div/p/strong/text()').getall(),
             'noticia-strong' : response.xpath('//div[@id="texto-int"]//div/strong/text()').getall(),
            'news': response.xpath('//div[@id="texto-int"]//div').getall(),
            'news_p': response.xpath('//div[@id="texto-int"]/p').getall(),
            'news_br': response.xpath('//div[@id="texto-int"]').getall()

        }


        return boletim






