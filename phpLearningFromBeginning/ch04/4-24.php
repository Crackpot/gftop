<?php
$olympic = array(
'Barcelona'=>1992,
'Atlanta'=>1996,
'Sydney'=>2000,
'Athens'=>2004,
'Beijing'=>2008
);

echo 'ԭ���飺';
echo '<pre>';
print_r($olympic);
echo '</pre>';

$nol = array_flip($olympic);
echo '<br/>';

echo '����Ԫ�غ������Ե�֮��';
echo '<pre>';
print_r($nol);
?>