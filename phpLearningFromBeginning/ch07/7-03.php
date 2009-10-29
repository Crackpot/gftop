<?php
$time = mktime(20,0,0,8,8,2008);

echo "<b>日期：".date("Y-m-d H:i:s",$time)."</b>";
echo "<br/>";

echo "<pre>";
echo "该日期相关信息如下：";
echo "<br/>";

$date = getdate($time);
print_r($date);
?>
