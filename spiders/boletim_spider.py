import scrapy

class BoletimSpider(scrapy.Spider):
    name = 'boletim'

    def start_requests(self):
        urls = []
        for i in range (1,84):
            urls.append('https://ufsj.edu.br/ascom/boletim{0:03}.php'.format(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, encoding='utf-8')

    def parse(self, response):
        boletim =  {
            'boletim-titulo' :  response.xpath('//p[@class="titulo-int2"]/text()').get(),
            'noticia-titulo' :  response.xpath('//div/p/strong/text()').getall(),
            'news': response.xpath('//div[@id="text-int"]//div').getall()

        }


        return boletim






