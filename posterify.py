import requests
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image,ImageFont,ImageDraw

print("Welcome to Posterify!")
text = input("What Poster would you like to make?\n")

search_url = "https://unsplash.com/s/photos/" + text

print("Searching for Image")

result = requests.get(search_url)
if result.status_code == 200:
    soup = BeautifulSoup(result.content, "html.parser")

f_image = soup.find('img', {'class': '_2zEKz'})

image_url = f_image['src']
filename = (text.replace(' ','_') + ".png").lower()

urllib.request.urlretrieve(image_url, filename)
print('Image Successfully Downloaded')

print("Writing Text")
img = Image.open(filename)
W = img.width
H = img.height
draw = ImageDraw.Draw(img)
w, h = draw.textsize(text)
font = ImageFont.truetype('Pillow/Tests/fonts/Avenir Next.ttc', W//12)

draw.text(((W - 8*w)/2, (H/6)), text, (255, 255, 255), font=font)
img.save(filename)

print("Poster Ready:", filename)

