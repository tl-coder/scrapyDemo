import scrapy
from first_scrapyPro.items import ResponseItem


class XmithcSpider(scrapy.Spider):
    name = 'xmithc'
    #allowed_domains = ['xm.ithc.cn/']
    #start_urls = ['http://xm.ithc.cn/']
    allowed_domains=['https://wenku.baidu.com/view/a59738a7b0717fd5360cdc75.html']
    start_urls=['https://wenku.baidu.com/view/a59738a7b0717fd5360cdc75.html']
    def parse(self, response,**kwargs):
        #res = response.xpath('//ul[@class="side-article-list"]/li/a/text()')
        res = response.xpath('//p/text()')
        for d in res:
            item = ResponseItem()
            item['info'] = d.extract()
            yield item