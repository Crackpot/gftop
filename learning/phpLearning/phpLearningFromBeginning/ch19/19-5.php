<?php
$width = 200;
$height =300;

$img =  imagecreatetruecolor($width,$height) or die("不支持GD图像处理");
$line_color = imagecolorallocate($img, 255, 255, 255);
$font_type ="C://WINDOWS//Fonts//SIMLI.TTF";    //获取TrueType字体，采用隶书字体

//“西游记”3个字16进制字符
$cn_char1 = chr(0xE8).chr(0xA5).chr(0xBF);
$cn_char2 = chr(0xE6).chr(0xB8).chr(0xB8);
$cn_char3 = chr(0xE8).chr(0xAE).chr(0xB0);

//“吴承恩著”4个字16进制字符
$cn_str = chr(0xE5).chr(0x90).chr(0xB4).chr(0xE6).chr(0x89).chr(0xBF).chr(0xE6).chr(0x81).chr(0xA9);
$cn_str .= " ".chr(0xE8).chr(0x91).chr(0x97);

imageline($img, 0, 40, 200, 40, $line_color);
imageline($img, 0, 260, 200, 260, $line_color);

//竖排显示“西游记”3字
imagettftext($img, 30, 0, 10, 80, $line_color, $font_type,$cn_char1);
imagettftext($img, 30, 0, 10, 120, $line_color, $font_type,$cn_char2);
imagettftext($img, 30, 0, 10, 160, $line_color, $font_type,$cn_char3);

//横排显示“吴承恩著”4字
imagettftext($img, 15, 0, 90, 254, $line_color, $font_type,$cn_str);

imagepng($img);
imagedestroy($img);
?>