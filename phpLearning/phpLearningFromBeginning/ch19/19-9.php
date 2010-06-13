<?php
function makeImageWaterMark($image,$pos,$water_text,$font_size,$color)
{
    $font_type ="C://WINDOWS//Fonts//cour.ttf";
    
    if(!empty($image) && file_exists($image))
    {
        $img_info = getimagesize($image);
        $g_w    = $img_info[0];     //取得背景图片的宽
        $g_h    = $img_info[1];     //取得背景图片的高

        switch($img_info[2])        //取得背景图片的格式
        {
            case 1:
                $img = imagecreatefromgif($image);
                break;
            case 2:
                $img = imagecreatefromjpeg($image);
                break;
            case 3:
                $img = imagecreatefrompng($image);
                break;
            default:
                die("图片格式错误！");
        }
    }
    else
    {
        die("需要加水印的图片不存在！");
    }
    
    //取得使用 TrueType 字体的文本的范围
    $temp = imagettfbbox(ceil($font_size*2.5),0,$font_type,$water_text);
    $w = $temp[2] - $temp[6];
    $h = $temp[3] - $temp[7];
    if(($g_w<$w) || ($g_h<$h))
    {
        echo "需要加水印的图片的大小比水印文字区域小，无法生成水印！";
        return;
    }
    
    //设置4种水印效果位置：0和默认是随机位置，1为顶端居左，2为中部居中，3为底端居右
    switch($pos)
    {
        case 0:
            $pos_x = rand(0,($g_w - $w));
            $pos_y = rand(0,($g_h - $h));
            break;
        case 1:
            $pos_x = 0;
            $pos_y = 0;
            break;
        case 2:
            $pos_x = ($g_w - $w)/2;
            $pos_y = ($g_h - $h)/2;
            break;
        case 3:
            $pos_x = $g_w - $w;
            $pos_y = $g_h - $h;
            break;
        default:
            $pos_x = rand(0,($g_w - $w));
            $pos_y = rand(0,($g_h - $h));
            break;
    }
    
    imagealphablending($img, true);    //设置图像混色模式
    
    if(!empty($color) && (strlen($color)==7))
    {
        $R = hexdec(substr($color,1,2));
        $G = hexdec(substr($color,3,2));
        $B = hexdec(substr($color,5));
    }
    else
    {
        die("水印文字颜色格式不正确！");
    }
    $text_color = imagecolorallocate($img, $R, $G, $B);
    
    imagettftext($img, $font_size, 0, $pos_x, $pos_y, $text_color, $font_type, $water_text);
    switch($img_info[2])                      //取得背景图片的格式 
    {
        case 1:
            imagegif($img,$image);
            break;
        case 2:
            imagejpeg($img,$image);
            break;
        case 3:
            imagepng($img,$image);
            break;
        default:
            die("不被支持格式的图片！");
    }
    
    imagedestroy($img);
}

if(isset($_FILES) && !empty($_FILES['userfile']) && $_FILES['userfile']['size']>0)
{
    $uploadfile = "./".time()."_".$_FILES['userfile']['name'];
    if (copy($_FILES['userfile']['tmp_name'], $uploadfile))
    {
        makeImageWaterMark($uploadfile,2,"Photo by Mac",16,"#43042A");
        echo "<img src=\"".$uploadfile."\" border=\"0\">";
    }
    else
    { 
        echo "文件上传错误！<br/>";
    }
}
?>

<html>
<head><title>19-9.php</title></head>
<body>

<form enctype="multipart/form-data" method="POST">
选择上传图片: <input name="userfile" type="file">
<input type="submit" value="上传">
</form>

</body>
</html>