#WAP to print number of days in a month
echo "Enter n for month:"
read n
case $n in
	1|3|5|7|8|10|12) echo "31 days";;
	4|6|9|11) echo "30 days";;
	2) echo "28 days";;
	*) echo "Enter valid choice";;
esac