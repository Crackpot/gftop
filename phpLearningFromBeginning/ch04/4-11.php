<?php
$planet = array(
'Earth',
'Venus',
'Mars',
'Jupiter',
'Saturn'
);

sort($planet);

foreach($planet as $key => $value)
{
    echo 'planet['.$key.']='.$value;
    echo '<br/>';
    echo '<br/>';
}
?>