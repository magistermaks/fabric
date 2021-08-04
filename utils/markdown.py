
# Copyright (c) 2020 magistermaks - MIT License (https://mit-license.org/)
# Internal utility

import os
import sys
import marko

class Strikethrough( marko.inline.InlineElement ):
    pattern = r'~~ *(.+?) *~~'
    parse_children = True

class StrikethroughExtension:
    elements = [Strikethrough]

markdown = marko.Markdown(extensions=[StrikethroughExtension])

def markdown_read(callback):
	args = sys.argv.copy()
	args.pop(0)

	if len(args) == 0:
		print("Warning: Nothing to parse!");

	for path in args:
		with open(path) as file:
			callback(path, markdown.parse(file.read()))
