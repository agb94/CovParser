import xml.etree.ElementTree as ET

def cobertura(path):
    tree = ET.parse(path)
    root = tree.getroot()
    hits = {}
    source_files = root.findall("./packages/package/classes/class")
    for source_file in source_files:
        filepath = source_file.attrib['filename']
        hits[filepath] = {}
        for line in source_file.findall("./lines/line"):
            hits[filepath][int(line.attrib['number'])] = int(line.attrib['hits'])
    return hits