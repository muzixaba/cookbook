#!bin/bash
echo "What colour is the traffic light"

# create menu
select colour in Red Amber Green Exit
do
    if [[ $colour != "Exit" ]]
    then
        echo "Colour is $colour"
    else
        exit 0
    fi
done