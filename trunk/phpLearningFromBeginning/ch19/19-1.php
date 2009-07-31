<?php
$width = 200;
$height =200;

$img =  imagecreatetruecolor($width,$height) or die("不支持GD图像处理");
imagepng($img);
imagedestroy($img);
?>