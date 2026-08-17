import qrcode

url=input("Enter the site address : ")

img=qrcode.make(url)

img.save("qrcode.png")
