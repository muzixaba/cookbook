#!bin/bash
echo "Enter a number"

# read user input
read x

if [[ $x -lt 10 ]]
then
    echo "Number less than 10"
elif [[ $x -gt 10 ]]
then
    echo "Number greater than 10"
else
    echo "Number is 10"
fi
