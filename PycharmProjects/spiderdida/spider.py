import  requests
from bs4 import BeautifulSoup
import os
import pytesseract
from PIL import  Image
import re

image_url='http://localhost:8080/tdd/checkcode/image.jsp'
dir='/opt/projects/pyproject'
if  not os.path.exists(dir):
    os.mkdir(dir)
os.chdir(dir)
r=requests.get(image_url)
img_content=r.content
file='checkcode.jpg'
if(os.path.exists(file)):
    os.remove(file)
with open(file,'ab') as img_object:
    img_object.write(img_content)
    img_object.flush()
image=Image.open('checkcode.jpg')
code=pytesseract.image_to_string(image)
print(code)
#####根据得到的验证码登录系统
code='&checkCode='+code
url='http://localhost:8080/tdd/login.action'
postdata={"loginName":"ddwl","password":"ddwl","checkCode":"2503","platfromFlag":"localhost:8080"}
data='?loginName=ddwl&password=ddwl&platformFlag=localhost:8080'
headers={'content-type': 'application/json'}
r=requests.post(url+data+code,headers=headers,data=postdata)

html=r.content
html_doc=str(html,'utf-8') #html_doc=html.decode("utf-8","ignore")
print(html_doc)
###进入主页爬取内容
main_url='http://localhost:8080/tdd/manager/manager_managerCenter.action'
r_main=requests.post(main_url,cookies=r.cookies)

if os.path.exists('main.txt'):
    os.remove('main.txt')
with open('main.txt','ab') as main_content:
    main_content.write(r_main.content)
    main_content.flush()
soup=BeautifulSoup(r_main.text,'html.parser',from_encoding='utf-8')
links=soup.find_all('a', href=re.compile(r"/tdd/\w+"))
print(links)
new_urls=set()
for link in links:
    url='http://localhost:8080'+link['href']
    new_urls.add(url)
print(new_urls)

if  os.path.exists('data.txt'):
    os.remove('data.txt')

with open('data.txt','w') as data_content:

    for url in new_urls:
        r_table=requests.post(url,cookies=r.cookies)
        soup_table=BeautifulSoup(r_table.text,'html.parser',from_encoding='utf-8')
        tags=soup_table.find_all('td')
        txt=[]
        for tag in tags:
            txt.append(tag.get_text())
        # print(soup_table.find_all('td'))
        data_content.write(str(txt))
    data_content.flush()