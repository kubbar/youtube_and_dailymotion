#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)/scripts/
python3 Y-abscbnnews.py > ../Y-abscbnnews.m3u8

echo m3u grabbed
