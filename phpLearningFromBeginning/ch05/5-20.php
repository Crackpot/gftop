<?php
$str = "first=php&second[]=string+functions&second[]=useing";
echo 'ԭ�ַ�����';
echo '<br/>';
echo $str;

parse_str($str);
echo '<br/>';
echo '<br/>';

echo '���������';
echo '<br/>';
echo 'first = '.$first;
echo '<br/>';
echo 'second[0] = '.$second[0];
echo '<br/>';
echo 'second[1] = '.$second[1];

parse_str($str,$input);
echo '<br/>';
echo '<br/>';

echo 'ָ�������������Ľ����';
echo '<br/>';
echo "input['first'] = ".$input['first'];
echo '<br/>';
echo "input['second'][0] = ".$input['second'][0];
echo '<br/>';
echo "input['second'][1] = ".$input['second'][1];
echo '<br/>';
?>