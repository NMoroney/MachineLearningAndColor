# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import PIL
import PIL.Image  

print("mlc - pixel color classifer :")

path_lut = "../../data/"
name_lut = "mlcolor_lut-rsvm-17-65x65x65.png"

lut = PIL.Image.open(path_lut + name_lut)
w1 = lut.size[0]
print(lut.size)

img = PIL.Image.open("Colorful_Bell_Peppers-512.JPG")

print(img.size)

classified = PIL.Image.new(mode="RGB", size=img.size)

wide, high = img.size[0], img.size[1]
for y in range(high) :
  print (y, end=' ', flush=True)
  for x in range(wide) :
    pixel = img.getpixel((x, y))
    rq = int(pixel[0] / 4)
    gq = int(pixel[1] / 4)
    bq = int(pixel[2] / 4)
    xq = bq
    yq = gq + (rq * w1)
    qrgb = lut.getpixel((xq, yq))
    classified.putpixel((x, y), (qrgb[0], qrgb[1], qrgb[2]))
print ('\n')

classified.save("Colorful_Bell_Peppers-512-classified.JPG")

