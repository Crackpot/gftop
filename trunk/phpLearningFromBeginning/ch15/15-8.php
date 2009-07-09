<?php
$test_preg = array(
"AK47",
"163.com",
"happy new year!",
"EX0000",
"007 in USA",
"abc123",
"TEST-abc-315",
"123654789",
"Euapa00!"
);

echo "<b>原数组：</b>";
echo "<pre>";
print_r($test_preg);
echo "</pre>";

$preg_arr = preg_grep("/^[A-Z].*[0-9]$/",$test_preg);
echo "<br>";
echo "<b>将原数组中以任意大写字母开头的、中间任意个字符、最后以数字结尾的字符串找出：</b>";
echo "<pre>";
print_r($preg_arr);
echo "</pre>";
?>