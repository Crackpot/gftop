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
        echo "'$str' ����P��p��H��h<br/><br/>";
    }
    else
    {
        echo "<b>'$str' ���� P��p��H��h</b><br/><br/>";
    }
    
    if(ereg('P',$str))
    {
        echo "��ereg()�� '$str' ƥ��'P'<br/><br/>";
    }
    else
    {
        echo "<b>��ereg()�� '$str' ��ƥ��'P'</b><br/><br/>";
    }
}
?> 