from PIL import Image

img = Image.open("python_image.jpg")
w, h = img.size
cropped_img = img.crop((50, 30, w, h-60))
cropped_img.show()
