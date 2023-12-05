# Source this file to make use of the aliases

export AOC_COOKIE="..." # get this from the cookies tab in network tools on the AOC website

alias aos="python3 main.py < input"
alias aot="python3 main.py < test"
alias aoc="aot; echo; aos"


function aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > input
    else
        curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%d/input` | sed 's/\/0/\//g')" > input
    fi
}
