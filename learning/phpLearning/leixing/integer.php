<?php
    $a=1234;//十进制数
    $b=-123;//负数
    $c=0123;//八进制数  输出时自动转成十进制数
    $d=0x1A;//十六进制数
    echo 'a=',$a,"<br/>";
    echo 'b=',$b,"<br/>";
    echo 'c=',$c,"<br/>";
    echo 'd=',$d,"<br/>";
    echo '整型数的字长和平台有关，尽管通常最大值是大约二十亿（32 位有符号）。PHP 不支持无符号整数。 <br/>';
    //例子 11-2. 八进制数的怪事
    var_dump(010978);// 010 octal = 8 decimal
    echo '<br/><strong>整数溢出</strong><br/>
    如果给定的一个数超出了 integer 的范围，将会被解释为 float。同样如果执行的运算结果超出了 integer 范围，也会返回 float。 <br/>';
    $large_number =  2147483647;
    var_dump($large_number);
    // 输出为：int(2147483647)

    $large_number =  2147483648;
    var_dump($large_number);
    // 输出为：float(2147483648)

    // 同样也适用于十六进制表示的整数：
    var_dump( 0x80000000 );
    // 输出为：float(2147483648)

    $million = 1000000;
    $large_number =  50000 * $million;
    var_dump($large_number);
    // 输出为：float(50000000000)
    echo '<br/>PHP 中没有整除的运算符。1/2 产生出 float  0.5。可以总是舍弃小数部分，或者使用 round() 函数。<br/>';
    var_dump(25/7);         // float(3.5714285714286)
    var_dump((int) (25/7)); // int(3)
    var_dump(round(25/7));  // float(4)
    echo'<br/><strong>转换为整形</strong><br/>
    要明示地将一个值转换为 integer，用 (int) 或 (integer) 强制转换。不过大多数情况下都不需要强制转换，因为当运算符，函数或流程控制需要一个 integer 参数时，值会自动转换。还可以通过函数 intval() 来将一个值转换成整型。<br/>

    <strong>从布尔值转换</strong><br/>
    FALSE 将产生出 0（零），TRUE 将产生出 1（壹）。<br/>
    
    <strong>从浮点数转换</strong><br/>
    当从浮点数转换成整数时，数字将被取整（丢弃小数位）。<br/>

    如果浮点数超出了整数范围（通常为 +/- 2.15e+9 = 2^31），则结果不确定，因为没有足够的精度使浮点数给出一个确切的整数结果。在此情况下没有警告，甚至没有任何通知！<br/>

    【译者注】在 Linux 下返回结果是最小负数（-2147483648），而在 Windows 下返回结果是零（0）。 <br/>
    
    警告<br/>
    决不要将未知的分数强制转换为 integer，这样有时会导致意外的结果。<br/>';
    echo (int) ( (0.1+0.7) * 10 ); // 显示 7！
    echo '<br/><strong>从其它类型转换</strong><br/>
    注意<br/>
    没有定义从其它类型转换为整型的行为。目前的行为和值先转换为布尔值一样。不过不要依靠此行为，因为它会未加通知地改变。';
?>
