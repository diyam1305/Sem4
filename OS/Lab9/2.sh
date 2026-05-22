#WAP to check whether the number is positive or negative
echo "Enter a:"
read a

if [ $a -gt 0 ]
then
	echo "$a is positive"
fi

if [ $a -lt 0 ]
then
	echo "$a is negative"
fi