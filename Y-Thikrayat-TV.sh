#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)/scripts/
python3 Y-Thikrayat-TV.py > ../Y-Thikrayat-TV.m3u8

echo m3u grabbed
