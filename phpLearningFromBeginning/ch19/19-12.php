<?php
$img_height=60; 
$img_width=20;

for($tmpa=0; $tmpa<4; ++$tmpa)
{
    $nmsg[$tmpa]=dechex(rand(0,15));            //生成随机数，并转成十六进制，作为验证码
}

$aimg = imagecreate($img_height,$img_width);    //生成图片
imagecolorallocate($aimg, 255,255,255);         //图片底色
$black = imagecolorallocate($aimg, 0,0,0);      //定义需要的黑色

//用黑色的矩形把图片包围
imagerectangle($aimg,0,0,$img_height-1,$img_width-1,$black);

//下面的代码生成底纹，其实就是在图片上生成一些符号
for($i=0; $i<100; ++$i)
{
    //使用*行号作为底纹，为了使底纹看起来杂乱无章、五颜六色，需要一个个地生成，同时其位置、颜色，大小都用随机数
    imagestring($aimg,1,mt_rand(1,$img_height),mt_rand(1,$img_width),"*",
    imagecolorallocate($aimg,mt_rand(200,255),mt_rand(200,255),mt_rand(200,255)));
}

//生成验证码，同样的道理，验证码一个个地输出到图片上，同时其位置、颜色，大小都用随机数
for($i=0; $i<count($nmsg); ++$i)
{
    imagestring($aimg, mt_rand(3,5),$i*$img_height/4+mt_rand(1,10),mt_rand(1,$img_width/4),
    $nmsg[$i],imagecolorallocate($aimg,mt_rand(0,100),mt_rand(0,150),mt_rand(0,200)));
}

header("Content-type: image/png");
imagepng($aimg);
imageiestroy($aimg);
?>


