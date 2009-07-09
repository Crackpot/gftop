<?php
$file = "data.txt";

if(is_dir($file))
{
    echo "文件 $file 是个目录";
    echo "<br/>";
}
else
{
    echo "文件 $file 不是目录";
    echo "<br/>";
}

if(is_file($file))
{
    echo "文件 $file 是一个普通文件";
    echo "<br/>";
}

if(is_readable($file))
{
    echo "文件 $file 是可读的";
    echo "<br/>";
}
else
{
    echo "文件 $file 是不可读的";
    echo "<br/>";
}

if(is_writeable($file))
{
   echo "文件 $file 是可写的";
   echo "<br/>";
}
else
{
   echo "文件 $file 是不可写的";
   echo "<br/>";
}
?>