#!/bin/bash

data=$(cat test.txt)
LINES=$(cat test.txt)

while read line; do
    echo "=== $line"
    # if word is command
    if [[ $line == "$ cd /" ]]
    then
        cd data 
        echo "Entering Data Path"
    elif [[ ${line:0:4} == "$ ls" ]]
    then
        echo "Doing nothing: ls"
    elif [[ $line == "$ cd .." ]]
    then
        cd ..
        echo "Going back a dir"
    elif [[ ${line:0:5} == "$ cd " ]]
    then 
        echo "Making Directory ${line:5}"
        mkdir ${line:5}
        cd ${line:5}
    elif [[ ${line:0:3} == "dir" ]]
    then
        echo "Looking at directory"
    else
        size=$(echo $line | tr -d -c 0-9)
        read -ra arr <<<"$line"
        file=${arr[1]}
        echo "Creating $file of size $size"
        
        dd if=/dev/zero of=$file bs=$size count=1
    fi
done < input.txt

cd "/home/al/aoc-2022/day7"
echo -n "Part1:      " 
find data -type d -exec sh -c "ls -goR {} | awk '/^-/{sum += \$3} END{print sum}' " \; | awk '$1<=100000{sum += $1} END{print sum}'

used=$(python3 part2.py)
echo "Used:       ${used}"
DISK_SIZE=70000000
NEED_FREE=30000000
current_free=$((DISK_SIZE-used))
to_delete=$((NEED_FREE-current_free))
echo "Free space: ${current_free}"
echo "To Delete:  ${to_delete}" 
echo -n "Part2:      "
find data -type d -exec sh -c "ls -goR {} | awk '/^-/{sum += \$3} END{print sum}' " \; | awk -v del=$to_delete '$1>=del' | sort -n | head -1
