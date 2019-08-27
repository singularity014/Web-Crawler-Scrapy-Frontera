import scrapy



class GoodReadsSpider(scrapy.Spider):
    # 1) identity
    name = 'goodreads'

    # 2) requests
    def start_requests(self):

        url = "https://www.goodreads.com/quotes?page=1"
        yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            yield {
                'text': quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                 'author':quote.xpath(".//div[@class='quoteText']/a/text()[1]").extract_first(),
                 'tags':quote.xpath(".//div[@class='greyText smallText left']/a/text()[1]").extract()            
            }

