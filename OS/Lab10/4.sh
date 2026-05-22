#WAP to print the day name based on the number(1-sunday, ...)
echo "Enter number(from 1-7):"
read num
if [ $num -eq 1 ]
then
	echo "Sunday"

elif [ $num -eq 2 ]
then
	echo "Monday"

elif [ $num -eq 3 ]
then
	echo "Tuesday"

elif [ $num -eq 4 ]
then
	echo "Wednesday"

elif [ $num -eq 5 ]
then

	echo "Thursday"
elif [ $num -eq 6 ]
then
	echo "Friday"

elif [ $num -eq 7 ]
then
	echo "Saturday"
	
else
	echo "Enter valid number"
fi