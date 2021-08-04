
# Copyright (c) 2020 magistermaks - MIT License (https://mit-license.org/)
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
		lines = file.readlines()
		lines = [line.rstrip("\n") for line in lines]

		for line in lines:
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
	

def error(msg, path):
	print(_red("error: ") + msg + _yellow(" from: ") + path)

