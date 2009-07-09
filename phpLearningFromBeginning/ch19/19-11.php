<?php
$img_name="tower.jpg";
$percent = 0.2;

$src_img=imagecreatefromjpeg($img_name);

$ow=imagesx($src_img);
$oh=imagesy($src_img);

$nw=$ow * $percent;
$nh=$oh * $percent;

$desc_img = imagecreatetruecolor($nw, $nh);
imagecopyresampled($desc_img,$src_img,0, 0, 0, 0, $nw, $nh, $ow, $oh);

imagejpeg($desc_img);
imagedestroy($desc_img);
imagedestroy($src_img);
?>