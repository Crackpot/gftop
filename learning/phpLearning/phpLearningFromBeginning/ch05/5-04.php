<?php
$str1 = "I'm learning programming with Perl";
$str2 = "PHP";

echo "替换前：".$str1;

$str = str_replace("Perl",$str2,$str1);
echo "<br/>";
echo "<br/>";

echo "替换后：".$str;
?>
