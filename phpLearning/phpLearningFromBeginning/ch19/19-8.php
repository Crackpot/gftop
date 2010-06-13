<?php
$img_info=getimagesize("tower.jpg");

for($i=0; $i<4; ++$i)
{
    echo $img_info[$i];
    echo "<br/>";
}
?>