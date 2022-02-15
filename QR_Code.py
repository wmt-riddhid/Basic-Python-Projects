import qrcode

data = "Hello !!! Welcome to QRCode generator python project...Congrulations :) You Scanned QRCode correctly..!"
img = qrcode.make(data)
img.save ("/home/wmt-riddhi/Basic-Python-Projects/new/myqrcode.png")