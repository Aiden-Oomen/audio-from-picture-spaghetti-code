import requests
from PIL import Image
from io import BytesIO
import mathpy
from result_scraper import *
from file_editing import *# so many files, my gawd
import os

APIKey = os.getenv("APIkey")

response=requests.get(
  "https://circles.minx28.repl.co/677290033253711874/circle.png",
  params={
    "size":200,
    "seed":"ghfjyfjyfjgf",
    "premodifiers":"0.9,1.3,0.5",
    "postmodifiers":"1,1,1"
    # You can remove any or all of these
  },
  headers={
    "Authorization": APIKey
  }
)

img=Image.open(BytesIO(response.content))

img.save("output.png")



im = Image.open('output.png')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 2))
r1, g1, b1 = rgb_im.getpixel((3, 4))
r2, g2, b2 = rgb_im.getpixel((5, 6))
r3, g3, b3 = rgb_im.getpixel((7, 8))
#r4, g4, b4 = rgb_im.getpixel((9, 10))
#r5, g5, b5 = rgb_im.getpixel((40, 41))
#r6, g6, b6 = rgb_im.getpixel((82, 83))
#r7, g7, b7 = rgb_im.getpixel((122, 123))
#r8, g8, b8 = rgb_im.getpixel((162, 163))
#r9, g9, b9 = rgb_im.getpixel((198, 199))
# with your 200px image, you can request pixels from [0,0] to [199,199]
pixels = im.load()


x = f'{r, g, b}' +  f'{r1, g2, b2}' + f'{r3, g3, b3}'# + f'{r4, g4, b4}' + f'{r5, g5, b5}' #+ f'{r6, g6, b6}' + f'{r7, g7, b7}' + f'{r8, g8, b8}'

with open ("log.log", "w") as f:
	f.write(f'{x}')

print(x)
#55 lines