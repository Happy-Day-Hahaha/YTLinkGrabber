#!/bin/bash

python3 -m pip install requests

tv_grep --output ./epg.xml --channel-id 新唐人亚太台 REGEXP https://raw.githubusercontent.com/iptv-pro/iptv-pro.github.io/main/epg/epg.xml
