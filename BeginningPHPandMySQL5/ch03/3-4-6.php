<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<?php
    $val=3.14;
    echo "val = $val"."&nbsp;其类型为：".gettype($val)."<br/>";
    settype($val,"string");
    echo "val = $val"."&nbsp;其类型为：".gettype($val)."<br/>";
    settype($val,"int");
    echo "val = $val"."&nbsp;其类型为：".gettype($val)."<br/>";
    settype($val,"float");
    echo "val = $val"."&nbsp;其类型为：".gettype($val)."<br/>";
    settype($val,"double");
    echo "val = $val"."&nbsp;其类型为：".gettype($val)."<br/>";
?>
