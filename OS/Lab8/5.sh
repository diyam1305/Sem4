echo "Enter n:"
read n
if [ $((n % 5)) -eq 0 ]
	then
		echo "$n is divisible by 5"
else
	echo "$n is not divisible by 5"
fi