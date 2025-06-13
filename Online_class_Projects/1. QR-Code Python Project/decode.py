# Program: QR-Code decoder

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/ekki1/OneDrive/Desktop/Online class_projects/QR-Code Python Project/myqrcode.png")
result = decode(img)

for qr in result:
    print(qr.data.decode('utf-8'))