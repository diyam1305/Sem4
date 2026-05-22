#WAP to find given year is leap or not [if year can be divisible by 4 but not divisible by 100 then it is leap year but if it is
#divisible by 400 then it is leap year]
echo "Enter year:"
read year

if [[ $((year % 4)) -eq 0 &&  $((year % 100)) -ne 0 ||  $((year % 400)) -eq 0 ]]
then
	echo "$year is a leap year"

else
	echo "$year is not a leap year"
fi