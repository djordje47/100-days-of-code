import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    'test22.gif', save_all=True, append_images=[images[1]], duration=800, loop=0
)
