<?php
$planet = array(
'Earth',
'Venus',
'Mars',
'Jupiter',
'Saturn'
);

echo '��ǰԪ���ǣ�'.current($planet);
echo '<br/>';

next($planet);
next($planet);

echo '<br/>';
echo '��������next����֮�󣬵�ǰԪ���ǣ�'.current($planet);
echo '<br/>';

reset($planet);

echo '<br/>';
echo 'reset����$planet�󣬵�ǰԪ���ǣ�'.current($planet);
echo '<br/>';
?>
