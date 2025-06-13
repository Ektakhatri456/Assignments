# Program: QR-Code encoder

import qrcode

data = "Hey beautiful soul!🌸 You just unlocked a secret message made with love by Ekta...Keep shining!✨"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill_color = "red", back_color = "white")

img.save("C:/Users/ekki1/OneDrive/Desktop/Online class_projects/QR-Code Python Project/myqrcode.png")



