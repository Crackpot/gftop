<?php
    // 这是最简单的类型。boolean 表达了真值，可以为 TRUE 或 FALSE。 
    //要指定一个布尔值，使用关键字 TRUE 或FALSE。两个都不区分大小写。 
    $foo=True;
    echo 'foo的类型：',gettype($foo),"<br/>";
    // 通常你用某些运算符返回 boolean 值，并将其传递给控制流程。 
    $action="show_version";
    if ($action=="show_version"){
        echo "The version is 1.23<br/>";
    }
    $show_separators=True;
    if ($show_separators){
        echo "separators<br>";
    }
    if($show_separators){
        echo "separators<br>";
    }
?>
<p > 要明示地将一个值转换成 boolean，用 (bool) 或者 (boolean) 来强制转换。但是很多情况下不需要用强制转换，因为当运算符，函数或者流程控制需要一个 boolean 参数时，该值会被自动转换。

参见类型戏法。 </p>
<p > 当转换为 boolean 时，以下值被认为是 FALSE：<BR/>
    *布尔值 FALSE<BR/>
    *整型值 0（零）<BR/>
    *浮点型值 0.0（零）<BR/>
    *空白字符串和字符串 "0"<BR/>
    *没有成员变量的数组<BR/>
    *没有单元的对象（仅适用于 PHP 4）<BR/>
    *特殊类型 NULL（包括尚未设定的变量）<BR/>
    所有其它值都被认为是 TRUE（包括任何资源）。<BR/>
    警告&nbsp;&nbsp;&nbsp;&nbsp;-1 和其它非零值（不论正负）一样，被认为是 TRUE！ <br/>
</p>
<?php
    echo '""==>',var_dump((bool) ""),'<br/>';
    echo '1==>',var_dump((bool) 1),'<br/>';
    echo '-1==>',var_dump((bool) -1),'<br/>';
    echo '"foo"==>',var_dump((bool) "foo"),'<br/>';
    echo '2.3e5==>',var_dump((bool) 2.3e5),'<br/>';
    echo 'array(12)==>',var_dump((bool) array(12)),'<br/>';
    echo 'array()==>',var_dump((bool) array()),'<br/>';
    echo '"false"==>',var_dump((bool) "false"),'<br/>';
?>