<?php
$day = 1;
$month = 10;
$year = 1949;

$national_unix = mktime(0,0,0,$month,$day,$year);
$now_unix = time();
$national_time = $now_unix - $national_unix;

$national_day_year = floor($national_time/(365*24*60*60));
$national_day_day = floor($national_time/(24*60*60));

echo "��������й�������1949-10-1�Ѿ�<b> ".$national_day_year." </b>��";
echo "<hr>";

echo "��������й�������1949-10-1�Ѿ�<b> ".$national_day_day." </b>��"
?>