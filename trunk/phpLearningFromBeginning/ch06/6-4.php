<?php
$fp = fopen($_SERVER['DOCUMENT_ROOT']."/../data/info.dat",'r');

if(!$fp)
{
    echo "<b>Error: ���ļ���������Ŀ¼�Ƿ���ȷ�����Ժ����ԣ�</b>";
    exit;
}

while(!feof($fp))
{
    $line = fgets($fp);
    echo $line;
    echo '<br/>';
}

fclose($fp);
?>