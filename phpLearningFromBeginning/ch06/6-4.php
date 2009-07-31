<?php
$fp = fopen($_SERVER['DOCUMENT_ROOT']."/../data/info.dat",'r');

if(!$fp)
{
    echo "<b>Error: 打开文件错误，请检查目录是否正确，或稍后再试！</b>";
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
