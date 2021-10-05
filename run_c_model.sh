#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH

cd ./data/$1

echo time eve 1 1 | getmodel | cdftocsv > dump.csv
