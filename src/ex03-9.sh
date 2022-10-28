str=$1
while read line;do
	if [[ "$line" =~ "$str" ]];then
		echo "$line"
	fi
done < DB.txt
exit 0
