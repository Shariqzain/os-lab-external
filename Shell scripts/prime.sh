is_prime() {
    num=$1

    if ((num<=1)); then
        echo "$num is not a prime number"
        return
    fi

    limit=$(echo "sqrt($num)" | bc)

    for ((i=2; i<=limit; i++)); do
        if ((num%i==0)); then
            echo "$num is not a prime number"
            return
        fi
    done

    echo "$num is a prime number"
}

read -p "Enter the number to check if its prime: " number
is_prime $number
