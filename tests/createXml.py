import copy
import sys
import xml.etree.ElementTree as ET

sys.path.append('..')
import core

def convertIntToChar(ints: list) -> list:
    """pega uma lista de inteiros e converte em uma lista de caracteres"""
    for x in range(len(ints)):
        ints[x] = chr(ints[x])
    return ints

def convertCharToInt(strs: list) -> list:
    """pega uma lista de caracteres e converte em uma lista de inteiros"""
    for x in range(len(strs)):
        strs[x] = ord(strs[x])
    return strs

def insertIdent(xml: bytes, indent: int=4) -> bytes:
    """pega dados com uma estrutura de um xml e insere um indentacao nos dados"""
    xml = convertIntToChar(list(xml))

    x = 0
    indentation = indent
    while x < len(xml)-1:
        if xml[x] == '>' and xml[x+1] == '<':
            if False:
                pass

            elif xml[x+2] != '/':
                xml = xml[:x+1] + list('\n' + (' ' * indentation)) + xml[x+1:]
                indentation += indent

            elif xml[x+2] == '/':
                indentation -= indent * 2
                xml = xml[:x+1] + list('\n' + (' ' * indentation)) + xml[x+1:]

        x += 1

    return bytes(convertCharToInt(xml))

def createXmlfile():
    """Cria um arquivo xml"""

    rss = ET.Element('rss')
    channel = ET.SubElement(rss, 'channel')
    item = ET.SubElement(channel, 'item')

    
    ET.SubElement(item, 'title').text = 'um titulo'
    ET.SubElement(item, 'link').text = 'um link'
    ET.SubElement(item, 'comment').text = 'um comentario'

    

    xml = ET.tostring(rss)
    xml = insertIdent(xml)
    with open('fileTest.xml', 'wb') as xmlFile:
        xmlFile.write(xml)

if __name__ == "__main__":
    createXmlfile()
