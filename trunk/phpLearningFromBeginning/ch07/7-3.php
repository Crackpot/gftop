<?php
$time = mktime(20,0,0,8,8,2008);

echo "<b>���ڣ�".date("Y-m-d H:i:s",$time)."</b>";
echo "<br/>";

echo "<pre>";
echo "�����������Ϣ���£�";
echo "<br/>";

$date = getdate($time);
print_r($date);
?>