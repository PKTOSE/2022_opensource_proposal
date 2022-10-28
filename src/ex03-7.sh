dir=$1
if [ ! -d $dir ]; then
    mkdir $dir
fi
cd $dir
for ((i=0;i<5;i++))
do	
	newdir="$dir$i"
	mkdir $newdir
	fname="$dir$i.txt"
	touch $fname
done
for ((i=0;i<5;i++))
do
	location="$dir$i.txt"
	todir="$dir$i/$location"
	ln -Tfs $location $todir
done
