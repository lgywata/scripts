import threading 
import xml.etree.ElementTree as ET

class myThread (threading.Thread):
    def __init__(self, filepath, failures):
        threading.Thread.__init__(self)
        self.filepath = filepath
        self.failures = failures

    def run(self):
        parsexml(self.filepath, self.failures)

def parsexml(filepath, failures):
    tree = ET.parse(filepath)
    root = tree.getroot()
    for package in root.findall('TestPackage'):
        packname = package.get('name')
        for test in package.getiterator('Test'):
            if test.get('result') == 'fail':
                testname = test.get('name')
                failures.append(packname + '|' + testname)

aosp = []
intel = []

file1 = myThread('/home/ywata/cts/cts-manta/without_patches/testResult.xml', aosp)
file2 = myThread('/home/ywata/cts/cts-manta/with_patches/testResult.xml', intel)

file1.start()
file2.start()

file1.join()
file2.join()

intelfailures = 0

for t in intel:
    if t not in aosp:
        print t
        intelfailures += 1

print "\nIntel failures only:", intelfailures

print "\n====================================================================\n"

aospfailures = 0

for t in aosp:
    if t not in intel:
        print t
        aospfailures += 1

print "\nAOSP failures only:", aospfailures
