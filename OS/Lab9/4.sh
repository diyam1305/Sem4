#WAP to check whether given 2 numbers are equal or not
echo "Enter a:"
read a
echo "Enter b:"
read b

if [ $a -eq $b ]
then
	echo "both the numbers are equal"
fi

if [ $a -ne $b ]
then
	echo "both the numbers are not equal"
fi