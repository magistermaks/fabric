
# Copyright (c) 2021 magistermaks - MIT License (https://mit-license.org/)
# Run: `python3 spellcheck.py path/to/file1.md path/to/file2.md <...>`

from utils import *

files = {}

def append( path, text ):
	if path in files:
		files[path] += " " + text
	else:
		files[path] = text

def process( path, ast ):

	if hasattr(ast, 'children'):
		if isinstance(ast.children, str):
			append(path, ast.children)
		else:
			for obj in ast.children:

				if isinstance(obj, marko.block.FencedCode):
					continue

				if isinstance(obj, marko.inline.CodeSpan):
					continue

				process(path, obj)

# begin execution
markdown_read(process)

exceptions = load_exceptions()

def check(error):
	if error in exceptions:
		return True

	if error.endswith("'s"):
		return error[:-2] in exceptions

	if error.endswith("s"):
		return error[:-1] in exceptions

	return False;

for path in files:

	# let's just give up on lawyer-speak
	if path.endswith("LICENSE.md"):
		continue

	output = shell("aspell --lang=en_US list", files[path]).lower().splitlines()

	for entry in output:
		if not check(entry):

			if entry == "todo" or entry == "fixme":
				warn(entry, path)
			else:
				try:
					suggestions = shell("aspell --lang=en_US pipe", entry).splitlines()[1].split(":")[1].strip().split(", ")[:3]
					suggestion = yellow(" did you mean: ") + " ".join(suggestions)
				except:
					suggestion = ""
					pass

				error(entry + suggestion, path)

die()

