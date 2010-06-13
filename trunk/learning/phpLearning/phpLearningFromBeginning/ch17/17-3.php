<?php
if(file_exists('17-1.xml'))
{
    $xml = simplexml_load_file('17-1.xml');
    var_dump($xml);
}
else
{
    exit('ÔØÈëÎÄ¼þtest.xmlÊ§°Ü');
}
?>