import qrcode
import image
qr =qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data='this is my first project after my python course completion.i am so much exited to do more projects and learn more... '

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('test.png') 