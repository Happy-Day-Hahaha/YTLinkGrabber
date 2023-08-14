#!/bin/bash

python3 -m pip install requests
sudo apt-get install xmltv-util

tv_grep --output ./epg.xml --channel-id 新唐人亚太台 REGEXP https://github.com/iptv-pro/iptv-pro.github.io/blob/main/epg/epg.xml
