<?php
if(file_exists('17-01.xml'))
{
    $xml = simplexml_load_file('17-01.xml');
    var_dump($xml);
}
else
{
    exit('载入文件test.xml失败');
}
?>
