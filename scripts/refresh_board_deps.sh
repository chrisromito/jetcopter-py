#!/usr/bin/env bash
# This Medium article illustrates the process/purpose here
#     https://medium.com/@chrismisztur/pycom-uasyncio-installation-94931fc71283
cd ~/jetcopter/esp/
rm -rf .deps
mkdir .deps
cd ./.deps
# Get the generic micropython lib
git clone https://github.com/micropython/micropython-lib.git micropython-lib

# Extract upip so we can use it on the device itself
echo "Moving to src/lib"
mv micropython-lib/upip/upip.py ../src/lib/upip.py
mv micropython-lib/upip/upip_utarfile.py ../src/lib/upip_utarfile.py
cd ..
echo "Done"
