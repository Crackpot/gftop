<?php
$str = "1fish2fish3fish4fish5fish";
echo "<b>�滻ǰ�ַ���Ϊ��</b><br/>";
echo $str;
echo "<br/>";
echo "<br/>";

$str_rpc = ereg_replace("[0-9]", " ", $str);
echo "<b>�滻���ַ���Ϊ��</b><br/>";
echo $str_rpc;
?>