import streamlit as st, qrcode, io
from PIL import Image

st.title('Hey, Enter URL to Generate QR Code')

url = st.text_input('Enter URL')

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)

    image = Image.open(io.BytesIO(imgByteArr.getvalue()))

    with st.columns(3)[1]:
     st.image(image)

if st.button('Submit'):
    output = generate_qr_code(url)
