import copy
import sys
import xml.etree.ElementTree as ET

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

def insertIdent(xml: bytes, INDENT: int=4) -> bytes:
    """pega dados com uma estrutura de um xml e insere um indentacao nos dados"""
    xml = convertIntToChar(list(xml))

    indent = INDENT
    x = 0
    while x < len(xml)-1:
        if xml[x] == '>' and xml[x+1] == '<' and xml[x+2] != '/':
            xml = xml[:x+1] + ['\n' + (' ' * indent)] + xml[x+1:]
            indent += INDENT

        elif xml[x] == '>' and xml[x+1] != '<':
            indent -= INDENT

        elif xml[x] == '>' and xml[x+1] == '<' and xml[x+2] == '/':
            indent -= INDENT
            xml = xml[:x+1] + ['\n' + (' ' * indent)] + xml[x+1:]
            
        x += 1
    
    xml = list(''.join(xml))
    return bytes(convertCharToInt(xml))

def createXmlStructure(size=1) -> bytes:
    """Cria a estrutura basica do xml para testes"""

    rss = ET.Element('rss')
    channel = ET.SubElement(rss, 'channel')
    item = ET.SubElement(channel, 'item')

    for x in range(size):
        ET.SubElement(item, 'title').text = f'titulo{x}'
        ET.SubElement(item, 'link').text = f'link{x}'
        ET.SubElement(item, 'comment').text = f'comentario{x}'
        ET.SubElement(item, 'pubDate').text = f'uma data{x}'

    return ET.tostring(rss)

def createXmlfile(FILENAME='filetest.xml', SIZE_ITEMS: int=1) -> None:
    """Cria um arquivo xml"""

    xml = createXmlStructure(SIZE_ITEMS)
    xml = insertIdent(xml)
    with open(FILENAME, 'wb') as xmlFile:
        xmlFile.write(xml)

if __name__ == "__main__":
    createXmlfile()
