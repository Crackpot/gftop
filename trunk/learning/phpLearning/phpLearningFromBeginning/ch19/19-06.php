<?php
$img=imagecreatefromjpeg("tower.jpg");

imagejpeg($img);
imagedestroy($img);
?>