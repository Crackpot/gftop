<?php
function makeImageWaterMark($image,$pos,$water_text,$font_size,$color)
{
    $font_type ="C://WINDOWS//Fonts//cour.ttf";
    
    if(!empty($image) && file_exists($image))
    {
        $img_info = getimagesize($image);
        $g_w    = $img_info[0];     //ȡ�ñ���ͼƬ�Ŀ�
        $g_h    = $img_info[1];     //ȡ�ñ���ͼƬ�ĸ�

        switch($img_info[2])        //ȡ�ñ���ͼƬ�ĸ�ʽ
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
                die("ͼƬ��ʽ����");
        }
    }
    else
    {
        die("��Ҫ��ˮӡ��ͼƬ�����ڣ�");
    }
    
    //ȡ��ʹ�� TrueType ������ı��ķ�Χ
    $temp = imagettfbbox(ceil($font_size*2.5),0,$font_type,$water_text);
    $w = $temp[2] - $temp[6];
    $h = $temp[3] - $temp[7];
    if(($g_w<$w) || ($g_h<$h))
    {
        echo "��Ҫ��ˮӡ��ͼƬ�Ĵ�С��ˮӡ��������С���޷�����ˮӡ��";
        return;
    }
    
    //����4��ˮӡЧ��λ�ã�0��Ĭ�������λ�ã�1Ϊ���˾���2Ϊ�в����У�3Ϊ�׶˾���
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
    
    imagealphablending($img, true);    //����ͼ���ɫģʽ
    
    if(!empty($color) && (strlen($color)==7))
    {
        $R = hexdec(substr($color,1,2));
        $G = hexdec(substr($color,3,2));
        $B = hexdec(substr($color,5));
    }
    else
    {
        die("ˮӡ������ɫ��ʽ����ȷ��");
    }
    $text_color = imagecolorallocate($img, $R, $G, $B);
    
    imagettftext($img, $font_size, 0, $pos_x, $pos_y, $text_color, $font_type, $water_text);
    switch($img_info[2])                      //ȡ�ñ���ͼƬ�ĸ�ʽ 
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
            die("����֧�ָ�ʽ��ͼƬ��");
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
        echo "�ļ��ϴ�����<br/>";
    }
}
?>

<html>
<head><title>19-9.php</title></head>
<body>

<form enctype="multipart/form-data" method="POST">
ѡ���ϴ�ͼƬ: <input name="userfile" type="file">
<input type="submit" value="�ϴ�">
</form>

</body>
</html>