#!/bin/bash

echo "You start with $# positional parameters"
counter=$#
serverIp=$(hostname -I |cut -d " " -f 1)
echo $serverIp
clientStrings=
newline=$'\n'

# Loop until all parameters are used up
while [ "$1" != "" ]; do
    echo "Parameter $counter equals $1"
    echo "You now have $# positional parameters"
    # Shift all the parameters down by one
    counter=$((counter - 1))
    parameters=" -s $serverIp -p $1 server"
    clientString+="checkConnection.py -s $serverIp -p $1 client ${newline}"
    python3 checkConnection.py $parameters &
    echo "--"
    shift

done

echo ""
echo ""
echo "create section to copy and paste for client"
echo ""
echo -e "$clientString"
echo ""
