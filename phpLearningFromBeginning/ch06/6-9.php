<?php
$file = "data.txt";
$dir = "info/newdata";

if(file_exists($file))
{
    echo "��ǰĿ¼�У��ļ�".$file."����";
    echo "<br/>";
}
else
{
     echo "��ǰĿ¼�У��ļ�".$file."������";
     echo "<br/>";
}
echo "<br/>";
echo "<hr>";
echo "<br/>";

if(file_exists($dir))
{
    echo "��ǰĿ¼�£�Ŀ¼".$dir."����";
    echo "<br/>";
}
else
{
     echo "��ǰĿ¼�£�Ŀ¼".$dir."������";
     echo "<br/>";
}
?>