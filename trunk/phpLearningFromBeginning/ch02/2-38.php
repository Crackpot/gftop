<?php
$var = "some text";

function test()
{
    $var = "some text in function";
    echo '这是局部变量$var：'.$var;
}

echo '这是全局变量$var：'.$var;
echo '<br/>';
echo '<br/>';
test();
?>
