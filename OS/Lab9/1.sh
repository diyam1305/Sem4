#WAP to find largest from 2 numbers (using if)
echo "Enter a:"
read a
echo "Enter b:"
read b

if [ $a -gt $b ]
then
	echo "$a is max"
fi

if [ $b -gt $a ]
then 
	echo "$b is max"
fi
