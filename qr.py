import qrcode as qr #import in pip

instagram_url="https://www.instagram.com/google/"  #Use your username or pin your url here
#generate the qr code 
qr= qr.QRCode(
    version=1,  #control the size of qrcode. higher number create larger codes
    error_correction=qr.constants.ERROR_CORRECT_L,  #create an error correction if the qr_reader reads it partially damaged
    box_size=10,
    border=4,
)

qr.add_data(instagram_url)   #the line add data to the qrcode
qr.make(fit=True)   #if the data given fits to be true then the line finalizes the code.

#create image for qrcode
img=qr.make_image(fill='black', back_color='white')  #The generated image of qr with color corrections

#save the image of the file
img.save("instagram_qr_code.png") 

print("Scan to be my new friend!")
img.show()
