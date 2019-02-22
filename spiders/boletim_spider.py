import scrapy

class BoletimSpider(scrapy.Spider):
    name = 'boletim'

    def start_requests(self):
        urls = []
        for i in range (89):
            urls.append('https://ufsj.edu.br/ascom/boletim{0:03}.php'.format(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        boletim =  {
            'title' :  response.xpath('//p[@class="titulo-int2"]/text()').get().encode('utf-8'),
            'news' :  response.xpath('//div/p/strong/text()').getall().encode('utf-8')
        }

        return boletim


