<?php
$str = "我有%d本%s方面的编程书籍。";

$str1 = sprintf($str,1,"PHP");
echo $str1;

echo "<br/>";
echo "<br/>";

$num = 4;
$lang = "C++";

$str2 = sprintf($str,$num,$lang);
echo $str2;
?>