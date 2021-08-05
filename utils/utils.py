
# Copyright (c) 2021 magistermaks - MIT License (https://mit-license.org/)
# Internal utility

import os
import sys
import marko
import subprocess


class Strikethrough( marko.inline.InlineElement ):
    pattern = r'~~ *(.+?) *~~'
    parse_children = True


class StrikethroughExtension:
    elements = [Strikethrough]


def markdown_read(callback):
	markdown = marko.Markdown(extensions=[StrikethroughExtension])
	args = sys.argv.copy()
	args.pop(0)

	if len(args) == 0:
		print("Warning: Nothing to parse!");

	for path in args:
		with open(path) as file:
			callback(path, markdown.parse(file.read()))


def load_exceptions():
	exceptions = []

	with open("utils/exceptions.dict") as file:
		for line in file.readlines():
			exception = line.rstrip("\n")

			if (len(exception) == 0) or (exception.startswith("#")):
				continue

			exceptions.append(exception)

	return exceptions


def shell(command, stdin):
	process = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
	return process.communicate(input=stdin.encode())[0].decode()


def _red(x):
	return "\033[31m" + x + "\033[0m"


def _yellow(x):
	return "\033[93m" + x + "\033[0m"


def warn(msg, path):
	print(_yellow("warning: ") + msg + _yellow(" from: ") + path)
	
_error_count = 0

def error(msg, path):
	global _error_count
	print(_red("error: ") + msg + _yellow(" from: ") + path)
	_error_count += 1

def die():
	if _error_count > 0:
		print("\nFound " + str(_error_count) + " errors!")
		exit(1)
	else:
		exit(0)

