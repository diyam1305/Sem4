#WAP to find maximum from 3 numbers 
echo "Enter a:"
read a
echo "Enter b:"
read b
echo "Enter c:"
read c

if [[ $a -gt $b && $a -gt $c ]]
then
	echo "$a is max"

elif [[ $b -gt $a && $b -gt $c ]]
then
	echo "$b is max"
	
else
	echo "$c is max"
fi
