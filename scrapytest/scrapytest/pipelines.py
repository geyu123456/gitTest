# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  os
import  requests
from scrapytest.items  import  ImageItem


class ScrapytestPipeline(object):
    print('enter piperline')
    count = 1
    pic_dir = '/opt/projects/pyproject/scrapytest/picture'
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)
    os.chdir(pic_dir)

    def process_item(self, item, spider):
        if isinstance(item,ImageItem):
            src=item['img_src']
            name='pic_'+str(self.count)
            with open(name+'.jpg','ab') as img_object:
                img_content=requests.get(src).content
                img_object.write(img_content)
                img_object.flush()
            self.count+=1

        return item
