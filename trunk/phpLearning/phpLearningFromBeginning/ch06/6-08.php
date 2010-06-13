<?php
$path = "/home/prog/php/sayHello.php";

$file_name = basename($path);
$dir_name = dirname($path);

echo "完整路径：".$path;
echo "<hr>";
echo "<br/>";

echo "其中目录名为：".$dir_name;
echo "<br/>";
echo "其中文件名为：".$file_name;
echo "<br/>";
?>
