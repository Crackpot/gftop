<?php
$str = "You have a car, I have a Car, We have cARs!";
echo "<b>替换前字符串为：</b><br/>";
echo $str;
echo "<br/>";
echo "<br/>";

$pattern = "car";
$replacement = "Apple";
$str_rpc = eregi_replace($pattern, $replacement, $str);
echo "<b>替换后字符串为：</b><br/>";
echo $str_rpc;
?>