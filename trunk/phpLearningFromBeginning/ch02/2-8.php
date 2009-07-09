<?php
$s = "this is a string";
$i = 9;
$arr = array(2,4,6);

is_string($s);    //返回TRUE，表示$s是一个字符串变量
is_string($i);    //返回FALSE，表示$i不是一个字符串变量
is_array($arr);   //返回TRUE，表示$arr是一个数组
is_array($s);     //返回FALSE，表示$s不是一个数组
?>