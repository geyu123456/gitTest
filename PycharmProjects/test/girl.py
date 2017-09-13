# coding:utf-8
import os
import requests
from bs4 import BeautifulSoup

root_url = 'http://iyangzi.com/?p=173'
response = requests.get(root_url)
if response.status_code == 200:
   girl_dir = '/opt/projects/pyproject'
if not os.path.exists(girl_dir):
    os.mkdir(girl_dir)
os.chdir(girl_dir)
soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
all_img = soup.find('div', class_='post-content').find_all('img')
count = 1
for img in all_img:
    src = img['src']
    # print src
    name = 'iyangzi' + str(count)
    with open(name + '.jpg', 'ab') as img_object:
        img_content = requests.get(src).content
        img_object.write(img_content)
        img_object.flush()
    count += 1