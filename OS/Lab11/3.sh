#WAP check a character is whether a vowel or consonant
echo "Enter character:"
read ch
case $ch in
	a|A|e|E|i|I|o|O|u|U) echo "Vowel";;
	*) echo "Consonant";;
esac