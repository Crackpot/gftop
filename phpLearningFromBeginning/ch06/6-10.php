<?php
$dir_name = "tmp_data";

if(mkdir($dir_name))    //在当前目录下创建目录tmp_data
{
    echo "目录".$dir_name."创建成功！";
    
    //在目录tmp_data中创建一个文件tmp.txt，并向其中写入一些内容
    if($fp = fopen($dir_name."/tmp.txt",'a'))
    {
        if(fwrite($fp,"Put Some Contenets into File."))
        {
            echo "<hr>";
            echo "在目录".$dir_name."下创建文件tmp.txt";
        }
    }
}
else
{
    echo "创建目录失败！";
    exit;
}
echo "<hr>";

if(rmdir($dir_name))    //尝试删除目录tmp_data
{
    echo "删除目录".$dir_name."成功！";
}
else
{
    echo "删除目录失败！";
    exit;
}
?>