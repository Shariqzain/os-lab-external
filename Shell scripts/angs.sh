check_armstrong() {
    local num=$1
    local original=$num
    local sum=0
    local num_digits=${#num}

    while ((num > 0)); do
        local digit=$((num % 10))
        local power_of_digit=1
        for ((i=0; i<num_digits; i++)); do
            power_of_digit=$((power_of_digit * digit))
        done
        sum=$((sum + power_of_digit))
        num=$((num / 10))
    done

    if ((original == sum)); then
        echo "$original is an Armstrong number."
    else
        echo "$original is not an Armstrong number."
    fi
}

read -p "Enter a number to check if it's an Armstrong number: " number
check_armstrong $number
