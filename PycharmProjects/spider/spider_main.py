import os
import requests
import html_downloader
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()

    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        count=1
        girl_dir='/opt/projects/pyproject'
        if not os.path.exists(girl_dir):
            os.mkdir(girl_dir)
        os.chdir(girl_dir)
        while self.urls.has_new_url():
         try:
            new_url=self.urls.get_new_url()
            print(new_url)
            html_cont=self.downloader.download(new_url)
            new_urls,img_srcs=self.parser.parse(new_url,html_cont)
            self.urls.add_new_urls(new_urls)
            for img in img_srcs:
                src=img['src']
                name='pic'+str(count)
                with open(name+'.jpg','ab') as img_object:
                    img_content=requests.get(src).content
                    img_object.write(img_content)
                    img_object.flush()
                    count+=1
         except ValueError:
             print('spider craw failed ')

if __name__=="__main__":
    root_url='http://iyangzi.com/?p=21'
    obj_Spider=SpiderMain()
    obj_Spider.craw(root_url)

