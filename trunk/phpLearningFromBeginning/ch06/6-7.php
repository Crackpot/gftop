<?php
$file = "data.txt";

if(is_dir($file))
{
    echo "�ļ� $file �Ǹ�Ŀ¼";
    echo "<br/>";
}
else
{
    echo "�ļ� $file ����Ŀ¼";
    echo "<br/>";
}

if(is_file($file))
{
    echo "�ļ� $file ��һ����ͨ�ļ�";
    echo "<br/>";
}

if(is_readable($file))
{
    echo "�ļ� $file �ǿɶ���";
    echo "<br/>";
}
else
{
    echo "�ļ� $file �ǲ��ɶ���";
    echo "<br/>";
}

if(is_writeable($file))
{
   echo "�ļ� $file �ǿ�д��";
   echo "<br/>";
}
else
{
   echo "�ļ� $file �ǲ���д��";
   echo "<br/>";
}
?>