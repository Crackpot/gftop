<?php
$dir = "D:\files";

//打开目录$dir，并将目录句柄赋给变量$dh
if($dh = opendir($dir))
{
    //通过while循环，使用函数readdir获取文件名
    while(($file_name = readdir($dh)) !== FALSE)
    {
        echo "file name: ".$file_name;
        echo "<br/>";
        echo "<br/>";
    }
    
    //处理完成后，关闭目录句柄$dh
    closedir($dh);
}
?>
