
from PIL import Image, ImageDraw, ImageFont
import json

size = 10
spacing = 34

font = ImageFont.truetype("DejaVuSansMono.ttf", size)


with open("json/test.json") as file:
	template = json.loads(file.read())

img = Image.new('RGBA', (template["width"], template["height"]), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

def draw_object(obj, draw, x, y):
	global size, spacing
	
	draw.rectangle( (x + 1, y + 1, x + size + 1, y + size + 1), fill=(255, 0, 0) )
	draw.text( (x + size + 4, y), obj["name"] + " (" + obj["type"] + ")", fill=(0, 0, 0), font=font )
	draw.text( (x + size + 4, y + size + 4), obj["text"], fill=(0, 0, 0), font=font )

	s = (size/2) + 1

	if len(obj["value"]) > 0:
		y2 = y

		for obj in obj["value"]:
			y2 += spacing
			draw_object(obj, draw, x + size + 4, y2)
			draw.line((x + s, y2 + s, x + size + 4, y2 + s), fill = (0,0,0))

		draw.line((x + s, y + size + 1, x + s, y2 + s), fill = (0,0,0))

draw_object(template["tree"], draw, 0, 0)
img.show()
