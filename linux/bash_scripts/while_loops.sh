#!bin/bash

i=0
while [ $SECONDS -lt 3 ]
do
  i=$((i+1))
done
echo $i