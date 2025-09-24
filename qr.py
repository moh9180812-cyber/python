import qrcode
img = qrcode.make ("https://instagram.com")
img.save("instagram.png","PNG")
