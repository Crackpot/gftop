<?php
$img_height=60; 
$img_width=20;

for($tmpa=0; $tmpa<4; ++$tmpa)
{
    $nmsg[$tmpa]=dechex(rand(0,15));            //�������������ת��ʮ�����ƣ���Ϊ��֤��
}

$aimg = imagecreate($img_height,$img_width);    //����ͼƬ
imagecolorallocate($aimg, 255,255,255);         //ͼƬ��ɫ
$black = imagecolorallocate($aimg, 0,0,0);      //������Ҫ�ĺ�ɫ

//�ú�ɫ�ľ��ΰ�ͼƬ��Χ
imagerectangle($aimg,0,0,$img_height-1,$img_width-1,$black);

//����Ĵ������ɵ��ƣ���ʵ������ͼƬ������һЩ����
for($i=0; $i<100; ++$i)
{
    //ʹ��*�к���Ϊ���ƣ�Ϊ��ʹ���ƿ������������¡�������ɫ����Ҫһ���������ɣ�ͬʱ��λ�á���ɫ����С���������
    imagestring($aimg,1,mt_rand(1,$img_height),mt_rand(1,$img_width),"*",
    imagecolorallocate($aimg,mt_rand(200,255),mt_rand(200,255),mt_rand(200,255)));
}

//������֤�룬ͬ���ĵ�����֤��һ�����������ͼƬ�ϣ�ͬʱ��λ�á���ɫ����С���������
for($i=0; $i<count($nmsg); ++$i)
{
    imagestring($aimg, mt_rand(3,5),$i*$img_height/4+mt_rand(1,10),mt_rand(1,$img_width/4),
    $nmsg[$i],imagecolorallocate($aimg,mt_rand(0,100),mt_rand(0,150),mt_rand(0,200)));
}

header("Content-type: image/png");
imagepng($aimg);
imageiestroy($aimg);
?>


