#!/usr/bin/python3

#
# Simple XML parser for JokesXML
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#
# Just prints the jokes in a JokesXML file

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string


def normalize_whitespace(text):
    "Remove redundant whitespace from a string"
    return " ".join(text.split())


class CounterHandler(ContentHandler):

    def __init__(self):
        self.inContent = False
        self.theContent = ""

    def startElement(self, name, attrs):
        if name == 'joke':
            self.title = normalize_whitespace(attrs.get('title'))
            print(" title: " + self.title + ".")
        elif name == 'start':
            self.inContent = True  # Lo que queremos leer es lo de dentro
        elif name == 'end':
            self.inContent = True  # Lo que queremos leer es lo de dentro

    def endElement(self, name):
        if self.inContent:
            self.theContent = normalize_whitespace(self.theContent)
        if name == 'joke':
            print()
        elif name == 'start':
            print("  start: " + self.theContent + ".")
        elif name == 'end':
            print("  end: " + self.theContent + ".")
        if self.inContent:
            self.inContent = False
            self.theContent = ""

    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


# --- Main prog

if len(sys.argv) < 2:
    print("Usage: python xml-parser-jokes.py <document>")
    print()
    print(" <document>: file name of the document to parse")
    sys.exit(1)

# Load parser and driver


JokeParser = make_parser()  # sabe reconocer el lenguaje y lo parsea
JokeHandler = CounterHandler()  # Manejador de los eventos para ese parse
JokeParser.setContentHandler(JokeHandler)

# Ready, set, go!

xmlFile = open(sys.argv[1], "r")
JokeParser.parse(xmlFile)

print("Parse complete")
