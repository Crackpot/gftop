<?php
    $variable1 = 13;
    echo "variable1 = $variable1"."&nbsp;&nbsp;&nbsp;";
    $variable2 = (double) $variable1;
    echo "variable2 = $variable2";

    echo "<br/>";
    $variable1 = 4.7;
    echo "variable1 = $variable1"."&nbsp;&nbsp;&nbsp;";
    $variable2 = 5;
    echo "variable2 = $variable2"."&nbsp;&nbsp;&nbsp;";
    $variable3 = (int) $variable1 + $variable2; // $variable3 = 9
    echo "variable3 = $variable3"."&nbsp;&nbsp;&nbsp;"."双精度数转换为整数类型时会出现误差"."<br/>";

    echo "<br/>";
    $variable1 = 1114;
    echo "variable1 = $variable1"."<br/>";
    $array1 = (array) $variable1;
    print "将variable1转换为数组类型之后，array1[0] = $array1[0]"."<br/>"; // The value 1114 is output.

    echo "<br/>";
    $sentence = "This is a sentence.";
    echo "sentence = $sentence"."<br/>";
    echo "将sentence转换为int类型时的值为：".(int) $sentence."<br/>"; // returns 0

    echo "<br/>";
    $model = "Toyota";
    echo "model = $model"."<br/>";
    $new_obj = (object) $model; // 将变量实例化
    print "new_obj->scalar = ".$new_obj->scalar; // returns "Toyota"
?>
