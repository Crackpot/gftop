<?php
$olympic = array(
'Barcelona'=>1992,
'AtLanTa'=>1996,
'sydney'=>2000,
'AthEns'=>2004,
'BEIJING'=>2008
);

echo 'ԭ���飺';
echo '<pre>';
print_r($olympic);
echo '</pre>';

$nol = array_change_key_case($olympic, CASE_UPPER);
echo '<br/>';

echo '����array_change_key_case()֮��';
echo '<pre>';
print_r($nol);
?>