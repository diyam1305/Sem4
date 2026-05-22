echo "Enter radius:"
read r
PI=3.14
area=$(echo "$PI*$r*$r" | bc)
echo "$area"