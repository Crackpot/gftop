<?php
$str = "K#V3050";
echo "<b>ԭ�ַ�����</b><br/>$str";
echo "<br/>";
echo "<br/>";

$reg_str = sql_regcase ($str);
echo "<b>ʹ�ú���sql_regcase()���ɵ�������ʽΪ��</b>";
echo "<br/>";
echo $reg_str;
?>