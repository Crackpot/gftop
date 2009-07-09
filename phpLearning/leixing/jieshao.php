<?php
    $bool=True;//a boolean
    $str="foo";//a string
    $int=12;//a integer
    echo "变量bool的类型：",gettype($bool),"<br/>";
    echo '变量str的类型：',gettype($str),"<br/>";
    echo '变量int的类型：',gettype($int),"<br/>";
    if (is_int($int)){
        $int+=4;
        echo 'int=',$int,"<br/>";
    }
    if(is_string($str)){
        $str+="haha";
        echo 'str=',$str,"<br/>";
    }
    if (is_bool($bool)){
        echo 'bool=',$bool,"<br/>";
    }
?>
<p> 如果要将一个变量强制转换为某类型，可以对其使用强制转换或者 settype() 函数。

注意变量根据其当时的类型在特定场合下会表现出不同的值。更多信息见类型戏法。</p>