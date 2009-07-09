<?php
$planet = array(
'Earth',
'Venus',
'Mars',
'Jupiter',
'Saturn'
);

echo '当前元素是：'.current($planet);
echo '<br/>';

next($planet);
next($planet);

echo '<br/>';
echo '调用两次next函数之后，当前元素是：'.current($planet);
echo '<br/>';

reset($planet);

echo '<br/>';
echo 'reset数组$planet后，当前元素是：'.current($planet);
echo '<br/>';
?>
