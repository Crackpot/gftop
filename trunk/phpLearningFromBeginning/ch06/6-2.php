<?php
$dir = "D:\files";

$file_list1 = scandir($dir);
//����scandir�����2�������������2������Ϊ1����ʾ����ĸ���������ļ���
$file_list2 = scandir($dir,1);

echo "<pre>";
print_r($file_list1);
print_r($file_list2);
?>