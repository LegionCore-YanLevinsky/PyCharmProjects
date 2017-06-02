from PIL import Image
from pyocr import tesseract

image = Image.open('en.jpg')
print(image)

print(tesseract.is_available())
# print(pytesseract.image_to_string(Image.open('en.jpg')))
