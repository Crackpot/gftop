<?php
if(checkdate(9,28,1980))
{
    echo "7,22,1978 : "."这是一个正确的日期格式";
}
else
{
    echo "这不是一个正确的日期格式";
}

echo "<br/>";
echo "<hr>";
echo "<br/>";

if(checkdate(9,99,1999))
{
    echo "这是一个正确的日期格式";
}
else
{
    echo "9,99,1999 : "."这不是一个正确的日期格式";
}
?>
