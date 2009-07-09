<?php
$str = 'jingle bells~, ';

echo '重复输出两次：';
echo '<br/>';
echo str_repeat($str,2);

echo '<br/>';
echo '<br/>';
echo '当函数str_repeat()第2个参数为0时：';
echo '<br/>';
echo 's='.str_repeat($str,0);
?>