<?php
$city_arr = array(
"ah"=>"合肥",
"fj"=>"福州",
"gs"=>"兰州",
"gd"=>"广州",
"gx"=>"南宁",
"gz"=>"贵阳",
"hn"=>"海口",
"hb"=>"石家庄",
"hh"=>"郑州",
"hl"=>"哈尔滨"
);

if(empty($_GET['prov']))
{
    echo iconv("GB2312","UTF-8",'<font color="red">您没有选择省（自治区）</font>');
}
else
{
    $prov = $_GET['prov'];
    $city = $city_arr[$prov];
    echo iconv("GB2312","UTF-8",'所选省（自治区）省会（首府）为：'.$city);
}
?>