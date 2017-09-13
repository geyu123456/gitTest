import spider_main
if __name__=="__name__":
    root_url='http://iyangzi.com/?p=21'
    obj_Spider=spider_main.SpiderMain()
    obj_Spider.craw(root_url)