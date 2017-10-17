var=$(<abc.txt)
vowels=$(echo $var | sed 's/[^aeiouAEIOU]//g')

echo "${#vowels} vowels"
