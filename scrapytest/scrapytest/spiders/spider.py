from bs4 import BeautifulSoup
import  scrapy
from scrapytest.items import ImageItem



class demoSpider(scrapy.Spider):
    print('enter spider')
    name="spider_girl"
    allowed_domain=["iyangzi.com"]
    start_urls=["http://iyangzi.com/?p=21"]
    def parse(self, response):
        print('start parse')
        soup=BeautifulSoup(response.text,'html.parser',from_encoding='utf-8')
        all_img=soup.find('div',class_='post-content').find_all('img')
        img_items=[]
        for img in  all_img:
            src=img['src']
            item=ImageItem()
            item['img_src']=src
            img_items.append(item)
        return img_items


