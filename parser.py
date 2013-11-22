import threading 
import xml.etree.ElementTree as ET

class myThread (threading.Thread):
    def __init__(self, filepath, total):
        threading.Thread.__init__(self)
        self.filepath = filepath
        self.total = total

    def run(self):
        parsexml(self.filepath, self.total)

total_1 = []
total_2 = []

def parsexml(filepath, total):
    tree = ET.parse(filepath)
    root = tree.getroot()
    packages = []
    tests = []
    results = []
    for package in root.findall('TestPackage'):
        packages.append(package.get('name'))
        for test in package.getiterator('Test'):
            if test.get('result') == 'fail':
                tests.append(test.get('name'))
                results.append(test.get('result'))
        packages.append(tests)
        packages.append(results)
        total.append(packages)
        break
    

file1 = myThread('testResult.xml', total_1)
file2 = myThread('testResult.xml', total_2)

file1.start()
file2.start()

file1.join()
file2.join()

for index, val in enumerate(total_1):
    print val[2]
    if 'false' not in val[2]:
        print "No failures for package: ", val[0]
    else:
        print "poutz..."
    break

print "Finished!\n"
