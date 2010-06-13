<?php
$str = "aaa~bbb~ccc~ddd";
echo "字符串截取前：$str";
echo "<br/>";
echo "<br/>";

$sep_arr = split("~",$str);
echo "<b>字符串截取后：</b><br/>";
echo "<pre>";
print_r($sep_arr);
?>