echo "Enter a:"
read a
echo "Enter b:"
read b
if [ $a -gt $b ]
	then
		echo "$a is largest"
else
	echo "$b is largest"
fi