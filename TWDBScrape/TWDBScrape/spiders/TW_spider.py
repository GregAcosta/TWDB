import scrapy	


class TWSpider(scrapy.Spider):
    name = "brands"
    allowed_domains = ['typewriterdatabase.com']
    start_urls = [
        "https://typewriterdatabase.com/all_manufacturers.php"
    ]


    def parse(self, response):
        for link in response.css('ol#masterList li div a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_table)


    def parse_table(self, response):
        for row in response.css('table'):
            for post in response.css('tr'):
                if response.css('td'):
                    yield {
                    'brand': response.css('h1::text')[0].get(),
                    'serialNum': post.css('td::text')[0].get(),
                    'yearMade': post.css('td::text')[1].get(),
                    'monthMade': post.css('td::text')[2].get(),
                    'dayMade': post.css('td::text')[3].get(),
                    'remarks': post.css('td::text')[4].get()
                }  


    def parse2(self, response):
        for link in response.css('ol ol li div a::attr(href)'):
           yield response.follow(link.get(), callback=self.parse_table2)


    def parse_table2(self, response):
        for row in response.css('table'):
           for post in response.css('tr'):
               if response.css('td'):
                   yield {
                    'brand': response.css('h1::text')[0].get(),
                    'serialNum': post.css('td::text')[0].get(),
                    'yearMade': post.css('td::text')[1].get(),
                    'monthMade': post.css('td::text')[2].get(),
                    'dayMade': post.css('td::text')[3].get(),
                    'remarks': post.css('td::text')[4].get()
                }  
