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
    echo 'Mars ����������$planet��';
    echo '<br/>';
    echo '<br/>';
}
if(in_array($temp,$planet))
{
    echo $temp.'����������$planet��';
    echo '<br/>';
    echo '<br/>';
}
else
{
    echo $temp.'������������$planet��';
    echo '<br/>';
    echo '<br/>';
}
?>
