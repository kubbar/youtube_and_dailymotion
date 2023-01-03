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
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:BANDWIDTH=290288,CODECS="mp4a.40.5,avc1.42c00b",RESOLUTION=256x144,FRAME-RATE=15,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
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
print('#EXT-X-STREAM-INF:BANDWIDTH=546239,CODECS="mp4a.40.5,avc1.4d4015",RESOLUTION=426x240,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
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
print('#EXT-X-STREAM-INF:BANDWIDTH=1209862,CODECS="mp4a.40.2,avc1.4d401e",RESOLUTION=640x360,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
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
print('#EXT-X-STREAM-INF:BANDWIDTH=1568726,CODECS="mp4a.40.2,avc1.4d401f",RESOLUTION=854x480,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
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
print('#EXT-X-STREAM-INF:BANDWIDTH=2969452,CODECS="mp4a.40.2,avc1.4d401f",RESOLUTION=1280x720,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
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
print('#EXT-X-STREAM-INF:BANDWIDTH=5420722,CODECS="mp4a.40.2,avc1.640028",RESOLUTION=1920x1080,FRAME-RATE=30,VIDEO-RANGE=SDR,SUBTITLES="vtt",CLOSED-CAPTIONS=NONE')
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
