from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# TODO 1: Buka gambar dengan Pillow
image = Image.open('C:\\Users\\daffa\\Downloads\\daffaakmal.jpg')

# TODO 2: Ubah tingkah kecerahan (brightness) dan kontras (contrast)
brightness_enhancer = ImageEnhance.Brightness(image)
brightened_image = brightness_enhancer.enhance(1.5)

contrast_enhancer = ImageEnhance.Contrast(brightened_image)
final_image = contrast_enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save('akmal.jpg')

# TODO 4: Tampilkan
plt.imshow(final_image)
plt.show()
