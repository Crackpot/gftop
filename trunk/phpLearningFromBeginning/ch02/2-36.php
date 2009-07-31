<?php
$i = 100;

function func($n)
{
    $n = $n+100;
}

echo "调用函数func前：\$i=$i";
echo "<br/>";
echo "<br/>";

func($i);
echo "调用函数func后：\$i=$i.<br/>";
?>
