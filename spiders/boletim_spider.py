import scrapy

class BoletimSpider(scrapy.Spider):
    name = 'boletim'

    def start_requests(self):
        urls = []

        for i in range (1,97):
            urls.append('https://ufsj.edu.br/ascom/boletim{0:03}.php'.format(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, encoding='utf-8')

    def parse(self, response):
        boletim =  {
            'boletim-titulo' :  response.xpath('//p[@class="titulo-int2"]/text()').get(),
            'noticia-titulo' :  response.css("p[id^='N']").xpath("strong").getall(),
            'news': response.xpath('//div[@id="texto-int"]').get(),

        }


        return boletim






