import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(file_name)

data_to_encode = "https://www.youtube.com/"
output_file_name = "qr_code.png"

generate_qr_code(data_to_encode, output_file_name)
print(f"QR-код успешно создан и сохранен в файл: {output_file_name}")