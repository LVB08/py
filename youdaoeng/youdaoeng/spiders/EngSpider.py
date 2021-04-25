from scrapy import Spider
import scrapy
import time
import re


class YoudaoengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 单词
    word = scrapy.Field()
    # 英式发音
    pron = scrapy.Field()
    # 发音audio文件链接
    pron_url = scrapy.Field()
    # 释义
    explain = scrapy.Field()
    # 例句
    example = scrapy.Field()
    # 发音 mp3 本地存放路径
    pron_save_path = scrapy.Field()

class EngSpider(Spider):
    name = "EngSpider"
    allowed_domains = ["dict.youdao.com"]

    start_urls = [
        'http://dict.youdao.com/w/eng/agree', 'http://dict.youdao.com/w/eng/prophet',
        'http://dict.youdao.com/w/eng/proportion']

    def parse(self, response):
        box = response.xpath('//*[@id="results-contents"]')
        word = YoudaoengItem()
        # 简明释义
        box_simple = box.xpath('.//*[@id="phrsListTab"]')
        # 判断查出来的字是否存在
        if box_simple:
            # 单词
            word['word'] = box_simple.xpath('.//h2[@class="wordbook-js"]//span[@class="keyword"]/text()').extract()[0]
            # 英式发音
            word['pron'] = box_simple.xpath(
                './/h2[@class="wordbook-js"]//div[@class="baav"]//*[@class="phonetic"]/text()').extract()[0]
            # 发音链接
            word['pron_url'] = "http://dict.youdao.com/dictvoice?audio=" + word['word'] + "&type=1"
            # 释义
            word['explain'] = []
            temp = box_simple.xpath('.//div[@class="trans-container"]//ul//li/text()').extract()
            for item in temp:
                if len(item) > 0 and not re.search(r'\n', item) and not re.match(r' ', item):
                    print(item)
                    word['explain'].append(item)
            # 例句
            time.sleep(3)
            word['example'] = []
            example_root = box.xpath('//*[@id="bilingual"]//ul[@class="ol"]/li')
            # 1.双语例句是否存在
            if example_root:
                for li in example_root:
                    en = ""
                    for span in li.xpath('./p[1]/span'):
                        if span.xpath('./text()').extract():
                            en += span.xpath('./text()').extract()[0]
                        elif span.xpath('./b/text()').extract():
                            en += span.xpath('./b/text()').extract()[0]
                    zh = str().join(li.xpath('./p[2]/span/text()').extract()).replace(' ', '')
                    word['example'].append(dict(en=en.replace('\"', '\\"'), zh=zh))
            #  2.柯林斯英汉双解大辞典的例句是否存在
            elif box.xpath('//*[@id="collinsResult"]//ul[@class="ol"]//div[@class="examples"]'):
                example_root = box.xpath('//*[@id="collinsResult"]//ul[@class="ol"]//li')
                for i in example_root:
                    if i.xpath('.//*[@class="exampleLists"]'):
                        en = i.xpath(
                            './/*[@class="exampleLists"][1]//div[@class="examples"]/p[1]/text()').extract()[0]
                        zh = i.xpath(
                            './/*[@class="exampleLists"][1]//div[@class="examples"]/p[2]/text()').extract()[0]
                        word['example'].append(dict(en=en.replace('\"', '\\"'), zh=zh))
                        if len(word['example']) >= 3:
                            break
            yield word
