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

echo 'ԭ���飺';
echo '<pre>';
print_r($say);
echo '</pre>';

$say_tmp = array_count_values($say);
echo '<br/>';

echo 'ͳ�ƽ�����£�';
echo '<pre>';
print_r($say_tmp);
?>