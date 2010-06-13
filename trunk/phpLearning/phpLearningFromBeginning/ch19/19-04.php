<?php
$width = 200;
$height =300;

$img =  imagecreatetruecolor($width,$height) or die("不支持GD图像处理");
$line_color = imagecolorallocate($img, 255, 255, 255);

imageline($img, 0, 40, 200, 40, $line_color);
imageline($img, 0, 260, 200, 260, $line_color);
imagestring($img, 5, 0, 60, "It's time to learn PHP!", $line_color);

imagepng($img);
imagedestroy($img);
?>