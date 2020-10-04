import xml.etree.ElementTree as ET

xml_file = ET.parse('./Task2/q-38.xml')
root = xml_file.getroot()

cnt = 0
ids = []
for child in root:
    nds = []
    for spec in child:
        if spec.tag == "nd":
            nds.append(spec)
    if nds[0].attrib["ref"] == nds[-1].attrib["ref"]:
        cnt += 1
        ids.append(child.attrib["id"])
with open("./Task2/poligons_ids.txt", "w") as f:
    f.write("Number of poligons: {}\n".format(cnt))
    for i in ids:
        f.write(i + '\n')