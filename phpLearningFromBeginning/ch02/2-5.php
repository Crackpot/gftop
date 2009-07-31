<?php
$foo = 10;

echo "转换前：\$foo=".$foo;
echo "<br/>";
echo "<br/>";

$foo = (boolean) $foo;
echo "转换后：\$foo=".$foo;
?>