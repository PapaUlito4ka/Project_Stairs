import xml.etree.ElementTree as ET

xml_file = ET.parse('./Task1/q-38.xml')
root = xml_file.getroot()

cnt = 0
ids = []
for child in root:
    for spec in child:
        if 'k' not in spec.attrib.keys() and 'v' not in spec.attrib.keys():
            continue
        if spec.attrib["k"] == "highway" and spec.attrib["v"] == "steps":
            cnt += 1
            ids.append(child.attrib["id"])
with open("./Task1/stairs_ids.txt", "w") as f:
    f.write("Number of stairs objects: {}\n".format(cnt))
    for i in ids:
        f.write(i + '\n')