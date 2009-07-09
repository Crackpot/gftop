<?php
$planet = array(
'Earth',
'Venus',
'Mars',
'Jupiter',
'Saturn'
);

$pos = current($planet);  //此时$pos=Earth

echo 'pos1='.$pos;
echo '<br/>';
echo '<br/>';

$pos = next($planet);     //此时$pos=Venus
echo 'pos2='.$pos;
echo '<br/>';
echo '<br/>';

$pos = current($planet);  //此时$pos=Venus
echo 'pos3='.$pos;
echo '<br/>';
echo '<br/>';

$pos = prev($planet);     //此时$pos=Earth
echo 'pos4='.$pos;
echo '<br/>';
echo '<br/>';

$pos = end($planet);      //此时$pos=Saturn
echo 'pos5='.$pos;
echo '<br/>';
echo '<br/>';

$pos = current($planet);  //此时$pos=Saturn
echo 'pos6='.$pos;
?>