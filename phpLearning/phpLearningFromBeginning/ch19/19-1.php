<?php
$width = 200;
$height =200;

$img =  imagecreatetruecolor($width,$height) or die("��֧��GDͼ����");
imagepng($img);
imagedestroy($img);
?>