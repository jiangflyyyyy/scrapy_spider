import scrapy

from MySpider.items import MyspiderItem


class YouwuSpider(scrapy.Spider):
    name = 'youwu'
    allowed_domains = ['youwu333.com']
    start_urls = ['https://www.youwu333.com/x/98/']

    def parse(self, response, **kwargs):
        tag_list = response.xpath('//div[@class="jigou"]/ul/li')
        item = MyspiderItem()
        for tag in tag_list:
            item['tag_name'] = tag.xpath('a/text()').get()
            item['tag_url'] = tag.xpath('a/@href').get()
            yield item
