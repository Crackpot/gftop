<?php
$file = "data.txt"; 
$content = "内容标题\r\n内容第一行\r\n内容第二行";    //要写入的内容

if(!$fp = fopen($file,'a'))                           //打开文件$file时，使用追加模式，此时文件指针会在文件开始处
{
    echo "打开文件$file失败！";
    exit;
}

if(fwrite($fp,$content) === FALSE)                    //将内容写入文件
{
    echo "写入文件失败！";
    exit;
}

echo "写入文件成功！";
fclose($fp);
?>
