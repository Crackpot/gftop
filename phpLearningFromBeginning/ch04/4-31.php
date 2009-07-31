<?php
$planet = array(
'Eth'=>'Earth',
'Vns'=>'Venus',
'Mrs'=>'Mars',
'Jpt'=>'Jupiter',
'Stn'=>'Saturn'
);

end($planet);
echo '当前元素的索引为：'.key($planet);
echo '<br/>';
echo '<br/>';
echo '当前元素的值为：'.end($planet);
?>
