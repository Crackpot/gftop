<?php
$planet1 = array(
'Earth',
'Venus',
'Mars',
'Jupiter',
'Saturn'
);

$planet2 = array(
'X'=>'Earth',
'Y'=>'Venus',
'Z'=>'Mars',
'A'=>'Jupiter',
'B'=>'Saturn'
);

asort($planet1);
ksort($planet2);

echo 'ʹ�ú���asort������Ԫ������';
echo '<br/>';

foreach($planet1 as $key => $value)
{
    echo 'planet1['.$key.']='.$value;
    echo '<br/>';
    echo '<br/>';
}

echo '<br/>';  
echo 'ʹ�ú���ksort������Ԫ������';
echo '<br/>';

foreach($planet2 as $key => $value)
{
    echo 'planet2['.$key.']='.$value;
    echo '<br/>';
    echo '<br/>';
}
?>