import xml.etree.ElementTree as ET
tree = ET.parse('testResult.xml')
root = tree.getroot()

aosp = []
for test in root.iter('Test'):
    result = test.get('result')
    if result == 'fail':
        aosp.append(test.get('name'))

tree = ET.parse('../with_patches/testResult.xml')
root = tree.getroot()

intel = []
for test in root.iter('Test'):
    result = test.get('result')
    if result == 'fail':
        intel.append(test.get('name'))

failed = 0
for t in intel:
    if t not in aosp:
        print t
        failed += 1

print "total Intel failures:", failed
