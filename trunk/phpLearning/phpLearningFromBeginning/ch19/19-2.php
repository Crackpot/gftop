<?php
$width = 200;
$height =200;

$img =  imagecreatetruecolor($width,$height) or die("��֧��GDͼ����");

$bg_color = imagecolorallocate($img, 255, 0, 0);
imagefill($img, 0, 0, $bg_color);

imagepng($img);
imagedestroy($img);
?>