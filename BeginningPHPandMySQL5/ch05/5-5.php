<h1>增加和删除数组元素</h1>

<h2>1.$arrayname[]</h2>
<p>通过赋值就能增加数组元素</p>
<?php
    $states["Ohio"] = "March 1, 1803";
    $states[] = "Ohio";
    echo "<pre>";
    print_r($states);
    echo "</pre>";

    echo "<br/>";
    echo "\$states[Ohio] = ".$states[Ohio]."<br/>";
    echo "\$states[\"Ohio\"] = ".$states["Ohio"]."<br/>";
    echo "\$states[0] = ".$states[0]."<br/>";
    echo "\$states[\"0\"] = ".$states["0"]."<br/>";
?>

<h2>2.array_push() <u>对比array_unshift()</u></h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states = array(
        "Ohio",
        "New York",
        );
    echo "原数组states为："."<br/>";
    print_r($states);
    echo "<br/>";

    echo "此操作对数组增加多个元素时，操作由元素列表从左向右进行从尾向头增加元素："."<br/>";
    echo "使用array_push向数组states增加元素California和Texas之后为："."<br/>";
    array_push($states,"California","Texas");
    print_r($states);
?>

<h2>3.array_pop() <u>对比array_shift()</u></h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states = array(
        "Ohio",
        "New York",
        "California",
        "Texas",
        );

    echo "原数组states为："."<br/>";
    print_r($states);
    echo "<br/>";

    echo "此操作将返回数组states的最后一个元素："."<br/>";
    echo "对数组states第一次使用array_pop减少元素后为："."<br/>";
    array_pop($states);
    print_r($states);
    echo "<br/>";

    echo "对数组states第二次使用array_pop减少元素后为："."<br/>";
    array_pop($states);
    print_r($states);
    echo "<br/>";

    echo "对数组states第三次使用array_pop减少元素后为："."<br/>";
    array_pop($states);
    print_r($states);
    echo "<br/>";

    echo "对数组states第四次使用array_pop减少元素后为："."<br/>";
    array_pop($states);
    print_r($states);
?>

<h2>4.array_shift() <u>对比array_pop()</u></h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states = array(
        "Ohio",
        "New York",
        "California",
        "Texas",
        );

    echo "原数组states为："."<br/>";
    print_r($states);
    echo "<br/>";

    echo "此操作将返回数组states的第一个元素而非最后一个："."<br/>";
    echo "对数组states第一次使用array_shift减少元素后为："."<br/>";
    array_shift($states);
    print_r($states);
    echo "<br/>";

    echo "对数组states第二次使用array_shift减少元素后为："."<br/>";
    array_shift($states);
    print_r($states);
    echo "<br/>";

    echo "对数组states第三次使用array_shift减少元素后为："."<br/>";
    array_shift($states);
    print_r($states);
    echo "<br/>";

    echo "对数组states第四次使用array_shift减少元素后为："."<br/>";
    array_shift($states);
    print_r($states);
?>

<h2>5.array_unshift() <u>对比array_push()</u></h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states = array(
        "Ohio",
        "New York",
        );

    echo "原数组states为："."<br/>";
    print_r($states);
    echo "<br/>";

    echo "此操作对数组增加多个元素时，操作由元素列表从右向左进行从头向尾增加元素："."<br/>";
    echo "对数组states使用array_unshift增加California和Texas后为："."<br/>";
    array_unshift($states,"California","Texas");
    print_r($states);
?>

<h2>6.array_pad()</h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states = array(
        "Alsaka",
        "Hawaii",
        );

    echo "原数组states为："."<br/>";
    print_r($states);
    echo "<br/>";

    echo "此操作会修改目标数组，将其大小增加到指定的长度："."<br/>";
    $states = array_pad($states,4,"New colony?");
    print_r($states);
    echo "<br/>";

    $states = array_pad($states,7,-222);
    print_r($states);
?>
