<?php
$str = 'PHP language programming in Web';
echo "<b>ԭ�ַ�����</b><br>";
echo $str;
echo "<br/><br/>";

$chars = preg_split('/ /', $str, -1, PREG_SPLIT_OFFSET_CAPTURE);
echo "<b>���ú���preg_split()��</b>";
echo "<pre>";
print_r($chars);
?>