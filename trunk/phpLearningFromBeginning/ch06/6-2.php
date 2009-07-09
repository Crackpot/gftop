<?php
$dir = "D:\files";

$file_list1 = scandir($dir);
//向函数scandir传入第2个参数，如果第2个参数为1，表示按字母降序排列文件名
$file_list2 = scandir($dir,1);

echo "<pre>";
print_r($file_list1);
print_r($file_list2);
?>