#! /usr/bin/python3

# Image Gallery Generator
#
# Author: Stefan Haun <tux@netz39.de>
#
# SPDX-License-Identifier: MIT
# License-Filename: LICENSES/MIT.txt

import xml.etree.ElementTree as ET

datafile = "mc-we.xml"

def printHtmlBegin(title, css):
    print("""
<!DOCTYPE html>
<html>
  <head>
    <title>{title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{css}" media="screen" />
  </head>
<body>
<div id="content">
    <h1>{title}</h1>
    """.format(title=title, css=css))

def printHtmlEnd():
    print("""
</div>
</body>
</html>
    """)

def printHtmlParagraph(content):
    print("""
    <p>{content}</p>
    """.format(content=content))

def printHtmlPicture(src, caption):
    print("""
    <div class="picture">
        <a href="{src}" target="_blank">
        <img src="{src}" alt="{caption}" />
        </a>
        <p>{caption}</p>
    </div>
    """.format(src=src, caption=caption))

if __name__ == '__main__':
    tree = ET.parse(datafile)
    root = tree.getroot()
    
    srctemplate = root.attrib['srctemplate']
    css = root.attrib['cssref']

    
    title = root.attrib['title']
    if title is None or title == "":
        title = "Some Gallery"
    
    printHtmlBegin(title, css)
    
    for child in root:
        if child.tag == "p":
            printHtmlParagraph(child.text)
        
        if child.tag == "picture":
            src = child.attrib['src']
            caption = child.attrib['caption']
            printHtmlPicture(srctemplate.format(src=src), caption)
    
    printHtmlEnd()

# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python; indend-pasted-text false; remove-trailing-space off
