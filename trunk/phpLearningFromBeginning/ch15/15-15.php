<?php
$str_arr = array(
"IAMEVERYSORRY",
"快乐编程，快乐生活",
"PHP编程",
"1997年香港回归",
"英语学习ABC",
"123456789"
);

$patt_ch = chr(0xa1) . "-" . chr(0xff);

foreach ($str_arr as $str)
{
    echo "字符串'$str' 是";
    if (preg_match("/^[$patt_ch]+$/", $str))
    {
        echo "<b>完全中文</b>";
        echo "<br>";
        echo "<br>";
    }
    else
    {
        echo "非完全中文";
        echo "<br>";
        echo "<br>";
    }
}
?>