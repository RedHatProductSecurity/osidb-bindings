#!/usr/bin/env bash
# Update bindings version in all places

# Increments the part of the string
# $1: version itself
# $2: number of part: 0 – major, 1 – minor, 2 – patch
function increment_version() {
    local version=($(echo "$1" | tr "." '\n'))
    version[$2]=$((version[$2]+1))
    echo $(local IFS="." ; echo "${version[*]}")
}


if [[ $1 =~ ^[0-9]+.[0-9]+.[0-9]+$ ]]; then
    echo "Replacing version in setup.py to $1"
    sed -i 's/version="[0-9]*\.[0-9]*\.[0-9]*"/version="'$1'"/g' setup.py

elif [[ $1 == "patch" ]]; then
    current_version=$(cat setup.py | grep -Po '(?<=version=\")\d+\.\d+\.\d+')
    new_version=$(increment_version $current_version 2)
    echo "Replacing version in setup.py to $new_version"
    sed -i 's/version="[0-9]*\.[0-9]*\.[0-9]*"/version="'$new_version'"/g' setup.py

else
    echo "invalid version $1"
    exit 1
fi

exit 0
