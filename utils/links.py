import os
import sys
import marko

links = []

def red(x):
	return "\033[31m" + x + "\033[0m"

def yellow(x):
	return "\033[93m" + x + "\033[0m"

def http( path ):
	# currently we just trust external links
	# but it would be nice to add some validation
	return True

class Strikethrough( marko.inline.InlineElement ):
    pattern = r'~~ *(.+?) *~~'
    parse_children = True

class StrikethroughExtension:
    elements = [Strikethrough]

def append( path, link ):
	if not link.startswith("http"):
		link = ("" if link.startswith("/") else os.path.dirname(path) + "/") + link;

	links.append( { 
		'link': link, 
		'path': path 
	} )

def process( path, ast ):

	if hasattr(ast, 'children'):
		for obj in ast.children :

			if isinstance( obj, Strikethrough ):
				return

			if isinstance( obj, marko.inline.Link ):
				append( path, obj.dest )
			else:
				process( path, obj )
	
markdown = marko.Markdown(extensions=[StrikethroughExtension])
sys.argv.pop(0)

for path in sys.argv:

	with open(path) as file:
		process( path, markdown.parse(file.read()) )

errors = 0

for entry in links:
	link = entry['link']

	if link.startswith("http"):
		if not http(link):
			errors += 1
			print(red("error: ") + link + yellow(" from: ") + entry['path'])
	else:
		if not os.path.exists( "./" + link ):
			errors += 1
			print(red("error: ") + link + yellow(" from: ") + entry['path'])

if errors > 0:
	print("\nFound " + str(errors) + " errors!")
	exit(1)
else:
	exit(0)

