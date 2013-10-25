import os
import sys

try:
    login = raw_input("Enter your login @master: ")
    # remote: ywata@master:/tmp
    remote = login + "@master:/tmp/apps"
    # use absolute path
    localdir = raw_input("Enter the directory you want to be rsynced (empty entry will use ./): ")

    if not localdir:
        localdir = "./"

    if not localdir.endswith('/'):
        localdir += '/'

    from subprocess import call
    call(["rsync", "-avz", remote, localdir])
    localdir += "apps/"
        
    androidmk = open(localdir + "Android.mk", "wb")
    androidmk.write("LOCAL_PATH := $(call my-dir)\n\n")

    devicemk = open("/home/ywata/workspace/build/target/product/generic_no_telephony.mk", "wb")
    devicemk.write("\n PRODUCT_PACKAGES += \\\n");

    apks = os.listdir(localdir)
    for apk in apks:
        if not apk.endswith(".apk"):
            continue
        androidmk.write("include $(CLEAR_VARS)\n")
        androidmk.write("LOCAL_MODULE := " + apk[:-4] + "\n")
        androidmk.write("LOCAL_SRC_FILES := " + apk + "\n")
        androidmk.write("LOCAL_MODULE_SUFFIX := .apk\n")
        androidmk.write("LOCAL_MODULE_CLASS := APPS\n")
        androidmk.write("LOCAL_CERTIFICATE := PRESIGNED\n")
        androidmk.write("LOCAL_MODULE_PATH := $(TARGET_OUT)/app\n")
        androidmk.write("include $(BUILD_PREBUILT)\n\n")
        
        devicemk.write("    " + apk[:-4] + " \\\n")

    androidmk.close()
    devicemk.close()

except KeyboardInterrupt:
    sys.exit()

