#!/bin/bash

## useful script when detecting other hosts in same LAN

for i in {1..255}
do
  x="192.168.0."$i
  arping $x -c 4
done
