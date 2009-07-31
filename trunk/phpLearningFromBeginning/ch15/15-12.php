<?php
$str = 'PHP language programming in Web';
echo "<b>原字符串：</b><br>";
echo $str;
echo "<br/><br/>";

$chars = preg_split('/ /', $str, -1, PREG_SPLIT_OFFSET_CAPTURE);
echo "<b>调用函数preg_split()后：</b>";
echo "<pre>";
print_r($chars);
?>