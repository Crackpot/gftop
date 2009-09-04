<h3>变量的作用域</h3>
<h5>1、局部变量</h5>
<?php
    $x = 4;
    function assignx(){
        $x = 0;
        echo "函数assignx内的\$x为:$x"."<br/>";
    }
    assignx();
    echo "函数assignx外的\$x为:$x"."<br/>";
?>

<h5>2、函数参数</h5>
<?php
    function x10($value){
        echo "传递进来的原参数为：$value"."<br/>";
        $value .= $value;
        return $value;
    }
    echo "函数的返回值为：".x10("Crackpot");
?>

<h5>3、全局变量</h5>
<?php
    $somevar = 15;
    echo "函数addit外，somevar is $somevar"."<br/>";
    $value = 2;
    echo "函数addit外，value is $alue"."<br/>";
    function addit(){
        GLOBAL $somevar;
        $somevar++;
        echo "函数内，somevar is $somevar"."<br/>";
        echo "函数内，value is $value"."<br/>";
    }
    addit();
?>

<h5>4、静态变量</h5>
<?php
    function keep_track(){
        STATIC $stcount = 0;
        $dycount = 0;
        $stcount ++;
        $dycount ++;
        echo "动态变量\$dycount值为：$dycount"."&nbsp;&nbsp;&nbsp;";
        echo "静态变量\$stcount值为：$stcount"."<br/>";
    }
    echo "静态变量每次初始化不会受到影响，动态变量则会被初始化掉"."<br/>";
    keep_track();
    keep_track();
    keep_track();
    keep_track();
?>
