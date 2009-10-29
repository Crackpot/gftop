<?php
$str = "1fish2fish3fish4fish5fish";
echo "<b>替换前字符串为：</b><br/>";
echo $str;
echo "<br/>";
echo "<br/>";

$str_rpc = ereg_replace("[0-9]", " ", $str);
echo "<b>替换后字符串为：</b><br/>";
echo $str_rpc;
?>