<?php
$i = 22;
$bi = 1011001;
$oi = 721;
$hi = A2;

echo "$i �Ķ��������ǣ�".decbin($i);
echo "<br/>";
echo "<br/>";
echo "$i �İ˽������ǣ�".decoct($i);
echo "<br/>";
echo "<br/>";
echo "$i ��ʮ���������ǣ�".dechex($i);
echo "<hr>";

echo "�������� $bi ��ʮ�������ǣ�".bindec($bi);
echo "<br/>";
echo "<br/>";
echo "�˽����� $oi ��ʮ�������ǣ�".octdec($oi);
echo "<br/>";
echo "<br/>";
echo "ʮ�������� $hi ��ʮ�������ǣ�".hexdec($hi);
echo "<hr>";

$hex_num = 'A515';
echo "ʹ�ú���base_convert()��ת��ʮ��������B515������������<br/>";
echo base_convert($hex_num,16,2);
?>