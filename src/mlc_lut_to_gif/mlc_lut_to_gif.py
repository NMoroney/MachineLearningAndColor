# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

from PIL import Image

def save_gif(frames, output, duration=100):
    frames[0].save(
        output,
        save_all = True,
        append_images=frames[1:],
        optimize=False,
        duration=duration,
        loop=0  # 0 for infinite loop
    )

path_lut = "../../data/"
# name_lut = "mlcolor_lut-rsvm-17-65x65x65.png"
name_lut = "mlcolor_lut-knn-11-65x65x65.png"

lut = Image.open(path_lut + name_lut)
print(lut.size)

n = 4
frames = []
dim = lut.size[0]
for i in range(dim):
  x1 = 0
  y1 = i * dim
  x2 = dim
  y2 = y1 + dim
  cropped = lut.crop((x1, y1, x2, y2))
  cropped = cropped.resize((dim * n, dim * n), Image.NEAREST)
  frames.append(cropped)

name_gif = name_lut[:-4] + ".gif"
save_gif(frames, name_gif)

