<?php
$str = "K#V3050";
echo "<b>原字符串：</b><br/>$str";
echo "<br/>";
echo "<br/>";

$reg_str = sql_regcase ($str);
echo "<b>使用函数sql_regcase()生成的正则表达式为：</b>";
echo "<br/>";
echo $reg_str;
?>