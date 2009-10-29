<?php
$day = 1;
$month = 10;
$year = 1949;

$national_unix = mktime(0,0,0,$month,$day,$year);
$now_unix = time();
$national_time = $now_unix - $national_unix;

$national_day_year = floor($national_time/(365*24*60*60));
$national_day_day = floor($national_time/(24*60*60));

echo "今天距新中国成立日1949-10-1已经<b> ".$national_day_year." </b>年";
echo "<hr>";

echo "今天距新中国成立日1949-10-1已经<b> ".$national_day_day." </b>天"
?>
