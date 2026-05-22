#WAP to check whether the number is odd or even
echo "Enter n:"
read n

if [ $((n % 2)) -eq 0 ]
	then
		echo "$n is even"
fi

if [ $((n % 2)) -ne 0 ]
then
	echo "$n is odd"
fi