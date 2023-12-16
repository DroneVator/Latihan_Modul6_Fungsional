from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('C:\\Users\\daffa\\Downloads\\daffaakmal.jpg')

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype('C:\\Users\\daffa\\Downloads\\Poppins.ttf', 200)
text = "Daffa Akmal, 266"
text_width = draw.textlength(text, font)
text_x = (gambarku.width - text_width) // 2
text_y = 20
draw.text((text_x, text_y), text, font=font, fill='white')

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
output_path = 'C:\\Users\\daffa\\Downloads\\test1.jpg'  # Ganti dengan path tempat Anda ingin menyimpan gambar hasil edit
gambarBW.save(output_path)

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
