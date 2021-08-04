
# Copyright (c) 2020 magistermaks - MIT License (https://mit-license.org/)
# Run: `python3 spellcheck.py path/to/file1.md path/to/file2.md <...>`

from markdown import *
from subprocess import Popen, PIPE, STDOUT

files = {}

def red(x):
	return "\033[31m" + x + "\033[0m"

def yellow(x):
	return "\033[93m" + x + "\033[0m"

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

exceptions = []
with open("utils/exceptions.dict") as file:
	lines = file.readlines()
	lines = [line.rstrip("\n") for line in lines]

	for line in lines:
		exception = line.rstrip("\n")

		if (len(exception) == 0) or (exception.startswith("#")):
			continue

		exceptions.append(exception)

def check(error):
	if error in exceptions:
		return True

	if error.endswith("'s"):
		return error[:-2] in exceptions

	if error.endswith("s"):
		return error[:-1] in exceptions

	return False;

errors = 0

for key in files:

	# let's just give up on lawyer-speak
	if key.endswith("LICENSE.md"):
		continue

	aspell = Popen(['aspell', '--lang=en_US', 'list'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
	output = aspell.communicate(input=files[key].encode())[0].decode().lower().splitlines()

	for error in output:
		if not check(error):
			type = red("error: ")

			if error == "todo" or error == "fixme":
				type = yellow("warning: ")
			else:
				errors += 1

			print(type + error + yellow(" from: ") + key)

if errors > 0:
	print("\nFound " + str(errors) + " errors!")
	exit(1)
else:
	exit(0)

