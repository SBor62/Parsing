import scrapy

class DivanSvetSpider(scrapy.Spider):
    name = 'divan_svet'
    allowed_domains = ['divan.ru']
    start_urls = ['https://www.divan.ru/saratov/category/svet']

    def parse(self, response):
        products = response.css('div._Ud0k')
        # Парсим все товары на странице
        for product in products:
            yield {
                'name': product.css('div.lsooF span::text').get(),
                'price' : product.css('div.pY3d2 span::text').get(),
                'url': product.css('a').attrib['href']
            }


