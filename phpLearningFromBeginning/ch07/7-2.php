<?php
echo "时间戳".mktime(0,0,0,12,31,2007)."对应的日期是：";
echo "<br/>";

echo date("M-d-Y", mktime(0,0,0,12,31,2007));
echo "<hr>";
echo "<br/>";

$day = 1;
echo "时间戳".mktime(0,0,0,7,$day+38,2008)."对应的日期是：<br/>";
echo date("Y-m-d", mktime(0,0,0,7,$day+38,2008));
echo "<hr>";
?>