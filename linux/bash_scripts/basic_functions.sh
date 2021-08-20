#!bin/bash
# declaring a basic function/method/procedure
display_string() {
    echo "This comes from a basic function"
}

# declaring function to return a string
function str_data() {
    the_string="string from str_data"
    echo $the_string
}

# function that reads input args
circle_area() {
    # read input arg(s)
    local radius=$1
    circle_area=$(echo $radius*$radius*3.14 | bc)
    # display area
    echo "If radius is $radius, area is $circle_area"
}

# invoke display_string function
display_string

# invoke str_data function
str_data

# display string data onto screen
echo $str_data

# read in radius value
echo "Enter circle radius size"
read rad

# invokde circle_area function
circle_area $rad