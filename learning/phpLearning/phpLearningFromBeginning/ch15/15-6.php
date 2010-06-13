<?php
$str = "AAAaaaA~BbbbC~DcccE~FdddZZZ";
echo "<b>字符串截取前：</b><br/>$str";
echo "<br/>";
echo "<br/>";

$sep_arr = split("[a-z]{3}",$str);
echo "<b>使用aaa，bbb，ccc，ddd做分割字符串后：</b>";
echo "<pre>";

print_r($sep_arr);
?>