cnt=0
while (( cnt < 3000 ))
do
	let cnt++
	adb -s $1 shell "ls /data"
        if [[  $? != 0 ]]; then
            echo "check failed"
            exit 1
        fi
done
echo "check ok"
