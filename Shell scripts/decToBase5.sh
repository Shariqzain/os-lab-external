decimal_to_base5() {
    echo -n "Base-5 of $1 is: "
    echo "obase=5; $1" | bc
}

read -p "Enter a decimal number: " number
decimal_to_base5 "$number"