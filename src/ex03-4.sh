echo "Is Linux Fun??(Y/N)"
read answer

case $answer in 
   yes|Y|Yes|YES|y|maybe|yeah|Yeah)
      echo "YES!";;
   
   [nN]*)
      echo "NO T.T";;
   
   *)
      echo "Please Enter Yes or NO!!";;
esac

exit 0
