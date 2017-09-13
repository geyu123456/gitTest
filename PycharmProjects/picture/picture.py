from PIL import  Image
import numpy as np
a=np.array(Image.open('pic78.jpg'))
b=[255,255,255]-a
im=Image.fromarray(b.astype('uint8'))
im.save('2.jpg')
