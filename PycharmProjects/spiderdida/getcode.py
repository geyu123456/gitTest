import  requests
from bs4 import BeautifulSoup
import os
import pytesseract
from PIL import  Image

url='http://dida.yesdididi.com/tdd/checkcode/image.jsp'
dir='/opt/projects/pyproject'
if  not os.path.exists(dir):
    os.mkdir(dir)
os.chdir(dir)
r=requests.get(url)
img_content=r.content
with open('checkcode.jpg','ab') as img_object:
    img_object.write(img_content)
    img_object.flush()
image=Image.open('checkcode.jpg')
code=pytesseract.image_to_string(image)
print(code)

