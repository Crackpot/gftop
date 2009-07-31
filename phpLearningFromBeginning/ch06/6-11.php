<?php
$dir_name = "tmp_data";
$new_file = "tmp_new.txt";

if(!copy($dir_name."/tmp.txt",$new_file))
{
    echo "Copy 文件tmp.txt失败";
    exit;
}

echo "文件tmp.txt拷贝成功";
echo "<br/>";
echo "<br/>";
echo "<hr>";
echo "<br/>";

if(unlink($new_file))
{
    echo "文件".$new_file."删除成功";
}
else
{
    echo "文件".$new_file."删除失败";
}
?>
