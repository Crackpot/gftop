<?php
$city_arr = array(
"ah"=>"�Ϸ�",
"fj"=>"����",
"gs"=>"����",
"gd"=>"����",
"gx"=>"����",
"gz"=>"����",
"hn"=>"����",
"hb"=>"ʯ��ׯ",
"hh"=>"֣��",
"hl"=>"������"
);

if(empty($_GET['prov']))
{
    echo iconv("GB2312","UTF-8",'<font color="red">��û��ѡ��ʡ����������</font>');
}
else
{
    $prov = $_GET['prov'];
    $city = $city_arr[$prov];
    echo iconv("GB2312","UTF-8",'��ѡʡ����������ʡ�ᣨ�׸���Ϊ��'.$city);
}
?>