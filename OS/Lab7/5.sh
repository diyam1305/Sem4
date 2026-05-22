echo "Enter Principle:"
read P
echo "Enter Rate:"
read R
echo "Enter Time:"
read T
SI=$(echo "($P*$R*$T)/100" | bc)
echo $SI