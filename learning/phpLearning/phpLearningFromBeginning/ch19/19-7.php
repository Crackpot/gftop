<?php
$img=imagecreatefromjpeg("tower.jpg");

$x = imageSX($img);
$y = ImageSY($img);
echo "图片tower.jpg的宽为：<b>$x</b> pixels";
echo "<br/>";
echo "<br/>";
echo "图片tower.jpg的高为：<b>$y</b> pixels";
?>