#!bin/bash
# Display args
echo "You entered $1 $2 $3"

# store args in operands
a=$1
b=$3
operator=$2

# run the calculation
if [[ $operator == "+" ]]
then
    ((result=$a+$b))
elif [[ $operator == "-" ]]
then
    ((result=$a+$b))
elif [[ $operator == "*" ]]
then
    ((result=$a*$b))
else
    ((result=$a/$b))
fi

# echo result
echo "$1 $2 $3 = $result"