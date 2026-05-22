#WAP to take 3 subject, calculate
echo "Enter subject1's marks:"
read sub1
echo "Enter subject2's marks:"
read sub2
echo "Enter subject3's marks:"
read sub3

ttl=$(echo "$sub1 + $sub2 + $sub3" | bc)
echo "Total is:$ttl"

per=$(echo "$ttl/3" | bc)
echo "Percentage is:$per"

if [ $per -ge 90 ]
then
	echo "A class"

elif [ $per -ge 80 ]
then
	echo "B class"

elif [ $per -ge 70 ]
then
	echo "C class"

elif [ $per -ge 60 ]
then
	echo "D class"

elif [ $per -ge 50 ]
then
	echo "E class"

elif [ $per -lt 50 ]
then
	echo "Fail"

else
	echo "Enter valid number"
fi