<?php
$say = array(
'Say',
'you',
'say',
'me',
'Say',
'it',
'together'
);

echo '原数组：';
echo '<pre>';
print_r($say);
echo '</pre>';

$say_tmp = array_count_values($say);
echo '<br/>';

echo '统计结果如下：';
echo '<pre>';
print_r($say_tmp);
?>