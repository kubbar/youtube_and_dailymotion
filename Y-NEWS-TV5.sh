#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)/scripts/
python3 Y-NEWS-TV5.py > ../Y-NEWS-TV5.m3u8

echo m3u grabbed
