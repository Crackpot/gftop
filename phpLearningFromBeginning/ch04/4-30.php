<?php
$planet = array(
'Earth',
'Venus',
'Mars',
'Jupiter',
'Saturn'
);

$temp = 'mars';

if(in_array('Mars',$planet))
{
    echo 'Mars 存在于数组$planet中';
    echo '<br/>';
    echo '<br/>';
}
if(in_array($temp,$planet))
{
    echo $temp.'存在于数组$planet中';
    echo '<br/>';
    echo '<br/>';
}
else
{
    echo $temp.'不存在于数组$planet中';
    echo '<br/>';
    echo '<br/>';
}
?>
