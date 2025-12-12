convert_to_binary() {
    local dec=$1
    local binary=""

    if ((dec == 0)); then
        echo "Binary equivalent: 0"
        return
    fi

    while ((dec > 0)); do
        local remainder=$((dec % 2))
        binary="$remainder$binary"
        dec=$((dec / 2))
    done

    echo "Binary equivalent: $binary"
}

read -p "Enter a decimal number to convert to binary: " number
convert_to_binary $number
