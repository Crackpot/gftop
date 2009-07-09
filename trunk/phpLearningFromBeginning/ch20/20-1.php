<?php
$template_file = "temp.html";

$fs = fopen($template_file,"r");
$content = fread($fs, filesize($template_file));
fclose($fs);

$content = print_page($content,"pagetitle","模板应用");
$page = print_page($content,"greetings","你好，这个页面由模板生成");
echo $page;

function print_page($temp_c,$temp_v,$str_c)
{
    return ereg_replace("\{".$temp_v."\}",$str_c,$temp_c);
}
?>