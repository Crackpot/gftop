<?php
$str = "AAAaaaA~BbbbC~DcccE~FdddZZZ";
echo "<b>�ַ�����ȡǰ��</b><br/>$str";
echo "<br/>";
echo "<br/>";

$sep_arr = split("[a-z]{3}",$str);
echo "<b>ʹ��aaa��bbb��ccc��ddd���ָ��ַ�����</b>";
echo "<pre>";

print_r($sep_arr);
?>