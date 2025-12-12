base5_to_decimal() {
    echo -n "Decimal of base-5 number $1 is: "
    echo "ibase=5; $1" | bc
}

read -p "Enter a base-5 number: " number
base5_to_decimal "$number"