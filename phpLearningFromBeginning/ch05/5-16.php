<?php
$str = "<b>I love PHP!</b>";
$str_entity = htmlentities($str);

echo "转换前：$str";
echo "<br/>";
echo "<br/>";

echo "转换后：$str_entity";
?>
