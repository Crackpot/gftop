<?php
$file = "data.txt";
$dir = "info/newdata";

if(file_exists($file))
{
    echo "当前目录中，文件".$file."存在";
    echo "<br/>";
}
else
{
     echo "当前目录中，文件".$file."不存在";
     echo "<br/>";
}
echo "<br/>";
echo "<hr>";
echo "<br/>";

if(file_exists($dir))
{
    echo "当前目录下，目录".$dir."存在";
    echo "<br/>";
}
else
{
     echo "当前目录下，目录".$dir."不存在";
     echo "<br/>";
}
?>