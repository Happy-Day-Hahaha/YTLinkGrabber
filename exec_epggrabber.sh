#!/bin/bash

python3 -m pip install requests
sudo apt-get install xmltv-util

tv_grep --output ./epg.xml --channel-id 新唐人亚太台 REGEXP ./epg_origin.xml
