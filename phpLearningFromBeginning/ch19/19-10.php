<?php
$img_name="tower.jpg";
$src_img=imagecreatefromjpeg($img_name);

$ow=imagesx($src_img);            //ȡ��ԭͼ�Ŀ�
$oh=imagesy($src_img);            //ȡ��ԭͼ�ĸ�

$nw=round($ow*200.0/$ow);         //������ͼ�Ŀ��
$nh=round($oh*200.0/$oh);         //������ͼ�ĸ߶�

$desc_img=imagecreate($nw, $nh);  //������ͼ

imagecopyresized($desc_img, $src_img, 0, 0, 0, 0, $nw, $nh, $ow, $oh);
imagejpeg($desc_img);

imagedestroy($desc_img);
imagedestroy($src_img);
?>