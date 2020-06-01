import glob
from PIL import Image

frames = []
imgs = glob.glob(r"c:/Work/Python/png2gif/png/*.png")

for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save('c:/Work/Python/png2gif/beam2.gif',
               format="GIF", append_images=frames[1:],
               save_all=True, duration= 700, loop=0)
