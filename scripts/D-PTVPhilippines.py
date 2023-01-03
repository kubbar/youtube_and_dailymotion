#! /usr/bin/python3

import requests
import os
import sys

proxies = {}
if len(sys.argv) == 2:
    proxies = {
                'http' : sys.argv[1],
                'https' : sys.argv[1]
              }

na = 'https://raw.githubusercontent.com/kubbar/youtube_and_dailymotion/main/notwork/notwork.m3u8'
def grab(line):
    try:
        _id = line.split('/')[4]
        response = s.get(f'https://www.dailymotion.com/player/metadata/video/{_id}', proxies=proxies).json()['qualities']['auto'][0]['url']
        m3u = s.get(response, proxies=proxies).text
        m3u = m3u.strip().split('\n')[1:]
        d = {}
        cnd = True
        for item in m3u:
            if cnd:
                resolution = item.strip().split(',')[2].split('=')[1]
                if resolution not in d:
                    d[resolution] = []
            else:
                d[resolution]= item
            cnd = not cnd
        #print(m3u)
        m3u = d[max(d, key=int)]    
    except Exception as e:
        m3u = na
    finally:
        print(m3u)

print('#EXTM3U')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=290288,CODECS="mp4a.40.5,avc1.42c00b",RESOLUTION=256x144,FRAME-RATE=15,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
s = requests.Session()
with open('../D-PTVPhilippines_info.txt') as f:
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
print('#EXT-X-STREAM-INF:BANDWIDTH=546239,CODECS="mp4a.40.5,avc1.4d4015",RESOLUTION=426x240,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
s = requests.Session()
with open('../D-PTVPhilippines_info.txt') as f:
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
print('#EXT-X-STREAM-INF:BANDWIDTH=1209862,CODECS="mp4a.40.2,avc1.4d401e",RESOLUTION=640x360,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
s = requests.Session()
with open('../D-PTVPhilippines_info.txt') as f:
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
print('#EXT-X-STREAM-INF:BANDWIDTH=1568726,CODECS="mp4a.40.2,avc1.4d401f",RESOLUTION=854x480,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
s = requests.Session()
with open('../D-PTVPhilippines_info.txt') as f:
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
print('#EXT-X-STREAM-INF:BANDWIDTH=2969452,CODECS="mp4a.40.2,avc1.4d401f",RESOLUTION=1280x720,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
s = requests.Session()
with open('../D-PTVPhilippines_info.txt') as f:
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
print('#EXT-X-STREAM-INF:BANDWIDTH=5420722,CODECS="mp4a.40.2,avc1.640028",RESOLUTION=1920x1080,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
s = requests.Session()
with open('../D-PTVPhilippines_info.txt') as f:
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
