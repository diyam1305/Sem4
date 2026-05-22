echo "Enter a:"
read a
echo "Enter b:"
read b
sum=$(echo "$a+$b" | bc)
echo "$sum"