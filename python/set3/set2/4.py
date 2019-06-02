import os
import xml.etree.ElementTree as ET

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path,'breakfast.xml')
tree = ET.parse(xml_file)
root=tree.getroot()

for child in root:
    for element in child:
        print(element.tag,":",element.text)