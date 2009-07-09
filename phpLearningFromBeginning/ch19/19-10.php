<?php
$img_name="tower.jpg";
$src_img=imagecreatefromjpeg($img_name);

$ow=imagesx($src_img);            //取得原图的宽
$oh=imagesy($src_img);            //取得原图的高

$nw=round($ow*200.0/$ow);         //计算新图的宽度
$nh=round($oh*200.0/$oh);         //计算新图的高度

$desc_img=imagecreate($nw, $nh);  //建立新图

imagecopyresized($desc_img, $src_img, 0, 0, 0, 0, $nw, $nh, $ow, $oh);
imagejpeg($desc_img);

imagedestroy($desc_img);
imagedestroy($src_img);
?>