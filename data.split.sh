#!/bin/bash
#
# This script splits huge data.csv file
# into one file per month group of files
#
###

# VARS
FILE="data/data.csv"
LINE=0
PREFIX_OLD=""

while read row; do
	if [[ $LINE == 0 ]]
	then
		HEADER=${row}
	else
		PREFIX=${row:0:7}
		if [[ $PREFIX != $PREFIX_OLD ]]
		then
			echo $HEADER > data/${PREFIX}-data.csv
		fi
		echo ${row} >> data/${PREFIX}-data.csv
	fi
	PREFIX_OLD=$PREFIX
	((LINE++))
done <${FILE}
