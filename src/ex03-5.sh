showInfo(){
   ls $1 
}

echo "Start Program.."

echo "Enter the Function.."

read input

showInfo $input

echo "Quit.."

exit 0
