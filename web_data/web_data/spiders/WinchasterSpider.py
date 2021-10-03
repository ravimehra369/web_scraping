import scrapy

class WinchasterSpider(scrapy.Spider):
    name = "win"
    Start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?c']



    def parse(self, response):
         for product in response.css('div.product-description'):
             try:

               yield {
                  'price': product.css('a.catalog-item-price::text').get(),
                  'title': product.css('a.catalog-item-name::text').get(),
                  'stock_status': product.css('span.out-of-stock:text').get(),
                  'manufacturer': product.css('a.catalog-item-brand:text').get(),
                   }

             except:

                 yield {
                     'price': 'sold-out',
                     'title': product.css('a.catalog-item-name::text').get(),
                     'stock_status': 'out_of_stock',
                     'manufacturer': product.css('a.catalog-item-brand:text').get(),
                 }






    next_page = response.css('a.Next').attrib['href']
    if next_page is not None:
         yield response.follow(next_page, callback=self.parse)
