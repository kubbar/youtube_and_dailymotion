#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)/scripts/
python3 Y-NET25TV.py > ../Y-NET25TV.m3u8

echo m3u grabbed
