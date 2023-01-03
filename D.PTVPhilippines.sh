#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)/scripts/
python3 D.PTVPhilippines.py > ../D.PTVPhilippines.m3u8

echo m3u grabbed
