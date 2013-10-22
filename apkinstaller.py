import os
import sys

login = raw_input("Enter your login @master: ")
# remote: ywata@master:/tmp
remote = login + "@master:/tmp/apks"

# use absolute path
localdir = raw_input("Enter the directory you want to be rsynced (empty entry will use ./): ")

if not localdir:
    localdir = "./"

from subprocess import call
call(["rsync", "-avz", remote, localdir])
localdir = localdir + "apks/"

apks = os.listdir(localdir)

print ', '.join(apks)
for apk in apks:
   from subprocess import call
   call(["adb", "install", localdir + apk])

