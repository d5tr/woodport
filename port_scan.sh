#!/bin/bash

echo 'Start scaning ...'
nc -nvz $1 21 22 > $1.txt 2>&1
tac $1.txt
rm -rf $1.txt