#!/usr/bin/env bash
cd ~/jetcopter/esp/scripts
source env.sh
esptool.py --chip esp32 --port $ESP_PORT erase_flash
