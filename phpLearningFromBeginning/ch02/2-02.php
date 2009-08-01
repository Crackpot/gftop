<?php
    $s = "new string";

    //下面双引号字符串中的符号"$"未做转义，因此$s将被替换成其变量的值
    $str_1 = "双引号指定的字符串，$s";
    $str_1_plus = "双引号括住的变量名可以直接输出其变量内容,如直接输出上面那句话-----$str_1";
    
    //下面双引号字符串中的符号"$"做了转义，因此$s原封不动，不会被替换为变量$s的值
    $str_2 = "双引号指定的字符串，\$s";

    //单引号字符串中的"$"不用做转义即可原样输出
    $str_3 = '单引号指定的字符串，$s';

    $str_4 = '单引号指定的字符串，\$s';

    //在双引号字符串中，输出$、"、\等特殊字符，需要做转义
    $str_5 = "在双引号字符串中，输出特殊字符：\$ \" \\ '";

    //在单引号字符串中，输出'，需要做转义
    $str_6 = '在单引号字符串中，输出特殊字符：$ " \ \'';

    echo $str_1 , "<br/>";
    echo $str_1_plus;
    echo "<br/>";
    echo "<br/>";
    
    echo $str_2;
    echo "<br/>";
    echo "<br/>";

    echo $str_3;
    echo "<br/>";
    echo "<br/>";

    echo $str_4;
    echo "<br/>";
    echo "<br/>";

    echo $str_5;
    echo "<br/>";
    echo "<br/>";

    echo $str_6;
?>
