#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)/scripts/
python3 Y-UNTVNewsandRescue.py > ../Y-UNTVNewsandRescue.m3u8

echo m3u grabbed
