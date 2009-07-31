#假设需要将所有ipaddr目录下的java文件，编码从gb2312转到utf8
#cd ipaddr
find ./ -type f -name "*.java"|while read line;do
echo $line
iconv -f GB2312 -t UTF-8 $line > ${line}.utf8
mv $line ${line}.gb2312
mv ${line}.utf8 $line
done
#上面脚本将当前ipaddr目录下的所有java文件，从gb2312转到utf8，原文保存为*.php.gb2312。
#如果需要删除原来的gb2312文件，只需执行：
find ./ -type f -name "*.gb2312" -exec rm -f {} \; 
