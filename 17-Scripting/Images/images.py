from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filterd_img = img.filter(ImageFilter.BLUR)
filterd_img.save('blur.png', 'png')
filterd_img.show()
print(img.mode)