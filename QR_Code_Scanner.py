from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/home/harshil/Desktop/Python Programs/answer.png')

result = decode(img)

print(result)