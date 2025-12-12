check_palindrome() {
    local num=$1
    local original=$num
    local reverse=0

    while ((num > 0)); do
        local remainder=$((num % 10))
        reverse=$(((reverse * 10) + remainder))
        num=$((num / 10))
    done

    if ((original == reverse)); then
        echo "$original is a palindrome number."
    else
        echo "$original is not a palindrome number."
    fi
}

read -p "Enter a number to check if it's a palindrome: " number
check_palindrome $number
