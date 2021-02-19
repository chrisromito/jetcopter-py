#!/usr/bin/env bash
cd ~/jetcopter/esp/
source ./scripts/env.sh
picocom $ESP_PORT -b 115200
