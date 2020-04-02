#!/usr/bin/python3

#
# Simple XML parser for JokesXML
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# SARO and SAT subjects (Universidad Rey Juan Carlos)
# 2009-2020
#
# Just prints the jokes in a JokesXML file

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string

<<<<<<< HEAD

def normalize_whitespace(text):
    "Remove redundant whitespace from a string"
    return " ".join(text.split())


class CounterHandler(ContentHandler):

    def __init__(self):
=======
class CounterHandler(ContentHandler):

    def __init__ (self):
>>>>>>> 0bf5ae57bdf8073ab4e5650955b144a9159be644
        self.inContent = False
        self.theContent = ""

    def startElement(self, name, attrs):
        if name == 'joke':
            self.title = attrs.get('title')
            print(" Title: " + self.title + ".")
        elif name == 'start':
<<<<<<< HEAD
            self.inContent = True  # Lo que queremos leer es lo de dentro
        elif name == 'end':
            self.inContent = True  # Lo que queremos leer es lo de dentro

    def endElement(self, name):
=======
            self.inContent = True
        elif name == 'end':
            self.inContent = True
            
    def endElement (self, name):
>>>>>>> 0bf5ae57bdf8073ab4e5650955b144a9159be644
        if self.inContent:
            self.theContent = self.theContent
        if name == 'joke':
            print()
        elif name == 'start':
            print("  Start: " + self.theContent + ".")
        elif name == 'end':
<<<<<<< HEAD
            print("  end: " + self.theContent + ".")
=======
            print ("  End: " + self.theContent + ".")
>>>>>>> 0bf5ae57bdf8073ab4e5650955b144a9159be644
        if self.inContent:
            self.inContent = False
            self.theContent = ""

    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


# --- Main prog
<<<<<<< HEAD

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
=======
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: python xml-parser-jokes.py <document>")
        print()
        print(" <document>: file name of the document to parse")
        sys.exit(1)
    
    # Load parser and driver
    JokeParser = make_parser()
    JokeHandler = CounterHandler()
    JokeParser.setContentHandler(JokeHandler)

    # Ready, set, go!
    xmlFile = open(sys.argv[1],"r")
    JokeParser.parse(xmlFile)
>>>>>>> 0bf5ae57bdf8073ab4e5650955b144a9159be644

    print("Parse complete")
