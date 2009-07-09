<?php
$string = "The quick brown fox jumped over the lazy dog.";
echo "原字符串：<br/>";
echo $string;
echo "<br/><br/>";

$patterns[0] = "/quick/";
$patterns[1] = "/brown/";
$patterns[2] = "/fox/";

$replacements[2] = "bear";
$replacements[1] = "black";
$replacements[0] = "slow";

$str1 = preg_replace($patterns, $replacements, $string);
echo "使用函数ksort()之前字符串替换为：<br/>";
echo $str1;
echo "<br/><br/>";

ksort($patterns);
ksort($replacements);

$str2 = preg_replace($patterns, $replacements, $string);
echo "使用函数ksort()之前字符串替换为：<br/>";
echo $str2;
echo "<br/><br/>";
?> 