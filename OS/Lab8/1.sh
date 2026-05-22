echo "Enter a:"
read a
echo "Enter b:"
read b
echo -e "1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division"
read choice
if [ $choice -eq 1 ]
	then 
		sum=$(echo "$a+$b" | bc)
		echo "$sum"
fi

if [ $choice -eq 2 ]
	then 
		sum=$(echo "$a-$b" | bc)
		echo "$sum"
fi

if [ $choice -eq 3 ]
	then 
		sum=$(echo "$a*$b" | bc)
		echo "$sum"
fi

if [ $choice -eq 4 ]
	then 
		sum=$(echo "$a\$b" | bc)
fi
