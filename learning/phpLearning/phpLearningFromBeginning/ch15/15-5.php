<?php
$str = "aaa~bbb~ccc~ddd";
echo "�ַ�����ȡǰ��$str";
echo "<br/>";
echo "<br/>";

$sep_arr = split("~",$str);
echo "<b>�ַ�����ȡ��</b><br/>";
echo "<pre>";
print_r($sep_arr);
?>