<?php
$a = "test string";
echo "通过\$GLOBALS来取变量值：".$GLOBALS['a'];
echo "<br/>";
echo "<br/>";

echo "当前执行脚本的文件名：".$_SERVER['PHP_SELF'];
echo "<br/>";
echo "<br/>";

echo "当前执行脚本所在的根目录：".$_SERVER['DOCUMENT_ROOT'];
echo "<br/>";
echo "<br/>";

echo "当前执行脚本的的绝对路径：".$_SERVER['SCRIPT_FILENAME'];
echo "<br/>";
echo "<br/>";
?>