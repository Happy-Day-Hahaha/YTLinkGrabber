#! /usr/bin/python3
import requests
import os

def grab(url, ch_name):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        with open(f'{ch_name}.m3u', 'w', encoding='utf-8') as file:
            file.write(f"### {ch_name}\n")
        return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end - tuner: end]:
            link = response[end - tuner: end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    with open(f'{ch_name}.m3u', 'w', encoding='utf-8') as file:
        file.write(f"{link[start: end]} {ch_name}\n")

with open('./youtubeLink.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('##'):
            continue
        if not line.startswith('https:'):
            line = line.split('=')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            ch_logo = line[2].strip()
            #with open(f'{ch_name}.m3u', 'w', encoding='utf-8') as file:
                #file.write('#EXTM3U\n')
                #file.write(f'\n#EXTINF:-1 tvg-name="{ch_name}" group-title="{grp_title}" tvg-logo="{ch_logo}", {ch_name}\n')
        else:
            grab(line, ch_name)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
