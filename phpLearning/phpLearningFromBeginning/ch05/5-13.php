<?php
$str = "##使用函数trim去掉字符串两端特定字符####";

$str1 = trim($str,"#");    //为函数trim传入第二个参数，trim将删除字符串$str两端的#字符

var_dump($str);
echo "<br/>";
var_dump($str1);
?>
