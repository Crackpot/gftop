<?php
$template_file = "temp.html";

$fs = fopen($template_file,"r");
$content = fread($fs, filesize($template_file));
fclose($fs);

$content = print_page($content,"pagetitle","ģ��Ӧ��");
$page = print_page($content,"greetings","��ã����ҳ����ģ������");
echo $page;

function print_page($temp_c,$temp_v,$str_c)
{
    return ereg_replace("\{".$temp_v."\}",$str_c,$temp_c);
}
?>