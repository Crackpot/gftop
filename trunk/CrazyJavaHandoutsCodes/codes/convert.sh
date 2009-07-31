find ./ -type f -name "*.html"|while read line;do
echo $line
iconv -f GBK -t UTF-8 $line > ${line}.utf8
mv $line ${line}.gb2312
mv ${line}.utf8 $line
done 
