<?php
$img=imagecreatefromjpeg("tower.jpg");

$x = imageSX($img);
$y = ImageSY($img);
echo "ͼƬtower.jpg�Ŀ�Ϊ��<b>$x</b> pixels";
echo "<br/>";
echo "<br/>";
echo "ͼƬtower.jpg�ĸ�Ϊ��<b>$y</b> pixels";
?>