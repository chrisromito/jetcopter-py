#!/usr/bin/env bash
cd ~/jetcopter/esp/scripts
source ./env.sh
# esptool.py --chip esp32 --port $ESP_PORT --baud 460800 write_flash -z 0x1000 esp32-idf4-20210202-v1.14.bin
esptool.py --chip esp32 --port $ESP_PORT --baud 460800 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin
