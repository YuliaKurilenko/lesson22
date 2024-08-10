from PIL import Image
import datetime
def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 500))
    image.save(image_path)
def povorot(image_path):
    image = Image.open(image_path)
    image = image.rotate(7, expand=True)
    image.save(image_path, quality=95)
    image.close()
povorot('image.jpg')
start = datetime.datetime.now()
image_path = f'image.jpg'
resize_image(image_path)
end = datetime.datetime.now()
print(end-start)

