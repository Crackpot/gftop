<?php
$str_arr = array(
"PHP 是优秀的Web脚本语言",
"Perl的文本处理功能很强大"
);

foreach($str_arr as $str)
{
    //模式定界符后面的修正符"i" 表示匹配时不区分大小写字母
    if(preg_match("/php/i", $str))
    {
        echo "在字符串' $str '中找到对'php'的匹配";
        echo "<br/>";
        echo "<br/>";
    }
    else
    {
        echo "在字符串' $str '中<b>未</b>找到对'php'的匹配";
        echo "<br/>";
        echo "<br/>";
    }
}
?>