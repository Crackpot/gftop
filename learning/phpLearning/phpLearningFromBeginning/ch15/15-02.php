<?php
$arr_str = array(
'Python',
'php',
'Perl',
'Ruby'
);

for($i=0; $i<4; ++$i)
{
    $str = $arr_str[$i];
    if(eregi('P|h', $str))
    {
        echo "'$str' 含有P、p、H或h<br/><br/>";
    }
    else
    {
        echo "<b>'$str' 不含 P、p、H或h</b><br/><br/>";
    }
    
    if(ereg('P',$str))
    {
        echo "在ereg()中 '$str' 匹配'P'<br/><br/>";
    }
    else
    {
        echo "<b>在ereg()中 '$str' 不匹配'P'</b><br/><br/>";
    }
}
?> 