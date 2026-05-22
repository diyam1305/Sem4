#WAP to print corresponding gender
echo "Enter gender:"
read gender
case $gender in
	m|M) echo "Male";;
	f|F) echo "Female";;
	*) echo "Enter valid choice";;
esac