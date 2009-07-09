<?
echo "<H3>通过http协议打开文件</H3>";
echo "<br/>";

//通过 http 协议打开文件
if(!($file = fopen("http://localhost/ch06/server_data.txt", "r")))
{
    echo "文件不能打开";
    exit;
}
while(!feof($file))
{
    $line = fgetss($file, 255);    //按行读取文件中的内容
    echo $line;
    echo "<br/>";
}

fclose($file);                     //关闭文件的句柄
?>