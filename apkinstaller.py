import os
import sys

# the path to de directory with the apks
path = sys.argv[1] 
if not path.endswith('/') :
    path = path + '/'

apks = os.listdir(path)
for apk in apks:
    from subprocess import call
    call(["adb", "install", path + apk])
