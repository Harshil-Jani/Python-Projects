import qrcode
data = "Harshil-Jani Search me on Github ! "
img = qrcode.make(data)
img.save("/home/harshil/Desktop/answer.png") #put in the path where you want QR Code stored.
