import qrcode as qrc
img= qrc.make("https://web.facebook.com/durjoy.das.58367116") #creating qr code
img.save("MY_PROFILE.png") #save qr code as image

import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,border=3
)
qr.add_data("https://web.facebook.com/hridita.angela")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
img.save("Hridi_Profile.png")
 
 

social_media_links=[
    "https://web.facebook.com/durjoy.das.58367116",
    "https://www.instagram.com/durjoy619/",
    "https://t.me/{Durjoy167}",
    "https://wa.me/{01797373835}"
]
combianed_link="\n".join(social_media_links)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(combianed_link)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="blue", back_color="white")
qr_img.save("social_media_qr_code.png")  # Save the QR code image
qr_img.show()  # Display the QR code image

