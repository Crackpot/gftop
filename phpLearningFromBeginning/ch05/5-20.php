<?php
$str = "first=php&second[]=string+functions&second[]=useing";
echo '原字符串：';
echo '<br/>';
echo $str;

parse_str($str);
echo '<br/>';
echo '<br/>';

echo '分析结果：';
echo '<br/>';
echo 'first = '.$first;
echo '<br/>';
echo 'second[0] = '.$second[0];
echo '<br/>';
echo 'second[1] = '.$second[1];

parse_str($str,$input);
echo '<br/>';
echo '<br/>';

echo '指定输出数组参数的结果：';
echo '<br/>';
echo "input['first'] = ".$input['first'];
echo '<br/>';
echo "input['second'][0] = ".$input['second'][0];
echo '<br/>';
echo "input['second'][1] = ".$input['second'][1];
echo '<br/>';
?>