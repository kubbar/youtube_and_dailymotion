#! /usr/bin/python3

banner = r'''
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = s.get(url, timeout=15).text
    if '.m3u8' not in response:
        response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/kubbar/youtube_and_dailymotion/main/notwork/notwork.m3u8')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/kubbar/youtube_and_dailymotion/main/notwork/notwork.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U')
print('#EXT-X-STREAM-INF')
s = requests.Session()
with open('../Y-PTVPhilippines_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
import re
import m3u8
from m3u8 import protocol
from m3u8.parser import save_segment_custom_value


def parse_iptv_attributes(line, lineno, data, state):
    # Customize parsing #EXTINF
    if line.startswith(protocol.extinf):
        title = ''
        chunks = line.replace(protocol.extinf + ':', '').split(',', 1)
        if len(chunks) == 2:
            duration_and_props, title = chunks
        elif len(chunks) == 1:
            duration_and_props = chunks[0]

        additional_props = {}
        chunks = duration_and_props.strip().split(' ', 1)
        if len(chunks) == 2:
            duration, raw_props = chunks
            matched_props = re.finditer(r'([\w\-]+)="([^"]*)"', raw_props)
            for match in matched_props:
                additional_props[match.group(1)] = match.group(2)
        else:
            duration = duration_and_props

        if 'segment' not in state:
            state['segment'] = {}
        state['segment']['duration'] = float(duration)
        state['segment']['title'] = title

        # Helper function for saving custom values
        save_segment_custom_value(state, 'extinf_props', additional_props)

        # Tell 'main parser' that we expect an URL on next lines
        state['expect_segment'] = True

        # Tell 'main parser' that it can go to next line, we've parsed current fully.
        return True


if __name__ == '__main__':
    PLAYLIST = """#EXTM3U
    #EXTINF:-1 timeshift="0" catchup-days="7" catchup-type="flussonic" tvg-id="channel1" group-title="Group1",Channel1
    http://str00.iptv.domain/7331/mpegts?token=longtokenhere
    """

    parsed = m3u8.loads(PLAYLIST, custom_tags_parser=parse_iptv_attributes)

    first_segment_props = parsed.segments[0].custom_parser_values['extinf_props']
    print(first_segment_props['tvg-id'])  # 'channel1'
    print(first_segment_props['group-title'])  # 'Group1'
    print(first_segment_props['catchup-type'])  # 'flussonic'    
