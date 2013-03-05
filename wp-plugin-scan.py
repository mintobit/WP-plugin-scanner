#!/usr/bin/env python

import argparse
import sys
import re

argParser = argparse.ArgumentParser()
argParser.add_argument('-s', '--scan', metavar='<website url>', help='scan website at <website url>')
argParser.add_argument('-u', '--update', type=int, metavar='<page number>', help='update the list of plugins from wordpress.org up to <page number>')
args = argParser.parse_args()

def _argumentsNumber():
	return len(sys.argv) - 1

def _isUrl(url):
	pattern = re.compile('^https?://[\w\d\-\.]+/(([\w\d\-]+/)+)?$')
	if p.match(url):
		return True
	else:
		return False