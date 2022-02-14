import qrcode

data = "Do not forget to subscribe"
img = qrcode.make(data)
img.save ("/home/wmt-riddhi/Basic-Python-Projects/new/myqrcode.png")