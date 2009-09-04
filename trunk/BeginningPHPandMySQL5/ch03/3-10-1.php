<h3>执行控制语句</h3>

<h5>1.declare()</h5>

<h5>2.return()</h5>
<?php
    function cubed($value){
        echo "计算".$value."的立方"."<br/>";
        return $value * $value * $value;
    }
    $answer = cubed(3);
    echo $answer;
?>
