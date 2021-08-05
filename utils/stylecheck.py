
# Copyright (c) 2021 magistermaks - MIT License (https://mit-license.org/)
# Run: `python3 stylecheck.py path/to/file1.md path/to/file2.md <...>`

from utils import *

def process(path, ast):

	if hasattr(ast, 'children'):
		for obj in ast.children:

			if isinstance(obj, marko.inline.InlineHTML):
				error("Unexpected InlineHTML", path)
				continue

			process(path, obj)

def has_link(ast):

	if hasattr(ast, 'children'):
		for obj in ast.children:

			if isinstance(obj, marko.inline.Link):
				return True

	else:
		return False

def document(path, ast):

	skip = True

	# the if the file name is all-caps ...
	for char in path.split("/")[-1].split(".")[0]:
		if not char.isupper():
			skip = False
			break;

	# ... if yes, skip it
	if skip:
		return

	if len(ast.children) >= 2:
		
		if not isinstance(ast.children[0], marko.block.Heading):
			error("Expected Heading at line 1", path)
		elif ast.children[0].level != 2:
			error("Expected Heading (level 2) at line 1", path)

		if not has_link(ast.children[1]):
			error("Expected Link(s) at line 2", path)

		process(path, ast)

	else:
		warn("Document too short to validate", path)

# begin execution
markdown_read(document)
die()

