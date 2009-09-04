<h1>遍历数组</h1>

<h2>1.key()</h2>
<?php
    $captial = array(
        "Ohio" => "Columbus",
        "Iowa" => "Des Moines",
        "Arizona" => "Phoenix",
        );

    echo "key()返回数组中位于当前指针位置的键元素"."<br/>";
    echo "数组captial为："."<br/>";
    print_r($captial);
    echo "<br/>";

    echo "<p>Can you name the captials of these states?</p>";
    while($key = key($captial)){//key()返回数组中位于当前指针位置的键元素
        echo $key."<br/>";
        next($captial);//每个key()调用不会推进指针，因此需要使用next()函数，这个函数的唯一作用就是完成推进指针的任务。
    }
?>

<h2>2.reset()</h2>
<?php
    echo "执行完成上一段代码时，指针指向数组captial的位置为："."<br/>";
    echo current($captial)."<br/>";

    echo "通过reset()函数，指针指向数组captial的位置为："."<br/>";
    reset($captial);
    echo current($captial)."<br/>";
    echo "很明显，reset()函数将captial的指针设置回数组的开始位置"."<br/>";
?>

<h2>3.each()</h2>
<?php
    each($captial);
?>

<h2>4.current()</h2>
<?php
    $fruits = array("apple","orange","banana",);
    echo "数组fruits为："."<br/>";
    print_r($fruits);
    echo "<br/>";

    $fruit = current($fruits);
    echo "当前指针指向元素为：$fruit"."<br/>";

    $fruit = next($fruits);
    echo "执行next()后，指针指向元素为：$fruit"."<br/>";

    $fruit = prev($fruits);
    echo "执行prev()后，指针指向元素为：$fruit"."<br/>";
?>

<h2>5.end()</h2>
<?php
    echo "当前指针指向元素为：$fruit"."<br/>";
    $fruit = end($fruits);
    echo "执行end()后，指针指向元素为：$fruit"."<br/>";
?>

<h2>6.next()</h2>
<?php
    $fruit = reset($fruits);
    echo "执行reset()后，指针指向元素的开始位置：$fruit"."<br/>";

    $fruit = next($fruits);
    echo "执行next()后，指针指向元素为：$fruit"."<br/>";

    $fruit = next($fruits);
    echo "执行next()后，指针指向元素为：$fruit"."<br/>";
?>

<h2>7.prev()</h2>
<?php
    echo "当前指针指向元素为：$fruit"."<br/>";

    $fruit = prev($fruits);
    echo "执行prev()后，指针指向元素的开始位置：$fruit"."<br/>";

    $fruit = prev($fruits);
    echo "执行prev()后，指针指向元素的开始位置：$fruit"."<br/>";
?>

<h2>8.array_walk()</h2>
<form name="form1" action="5-7-submitdata.php" method="post">
    <p>
    Provide up to six keywords that you believe describe the state in whitch you live:
    </p>
    <p>Keyword 1 :
    <input type="text" name="keyword[]" size="20" maxlength="20" value=""/></p>
    <p>Keyword 2 :
    <input type="text" name="keyword[]" size="20" maxlength="20" value=""/></p>
    <p>Keyword 3 :
    <input type="text" name="keyword[]" size="20" maxlength="20" value=""/></p>
    <p>Keyword 4 :
    <input type="text" name="keyword[]" size="20" maxlength="20" value=""/></p>
    <p>Keyword 5 :
    <input type="text" name="keyword[]" size="20" maxlength="20" value=""/></p>
    <p>Keyword 6 :
    <input type="text" name="keyword[]" size="20" maxlength="20" value=""/></p>
    <p><input type="submit" value="submit"></p>
</form>

<h2>9.array_reverse()</h2>
<?php
    $states = array("Delaware","Pennsylvania","New Jersey",);
    echo "数组states为："."<br/>";
    print_r($states);

    echo "<br/>";
    echo "数组states经array_reverse处理后为："."<br/>";
    print_r(array_reverse($states));
    #array_reverse($states);

    echo "<br/>";
    echo "此时，数组states为："."<br/>";
    print_r($states);

    echo "<br/>";
    echo "可见，array_reverse()函数并不会改变原数组的顺序。"."<br/>";
    echo "并且，array_reverse()函数不会改变关联数组的顺序，其键映射总是会保持。"."<br/>";
?>

<h2>10.array_flip()</h2>
<?php
    $states = array("Delaware","Pennsylvania","New Jersey",);
    echo "数组states为："."<br/>";
    print_r($states);
    echo "<br/>";

    $states = array_flip($states);
    echo "数组states经过array_flip处理后为："."<br/>";
    print_r($states);
    echo "<br/>";
    echo "array_flip()函数会使数组中键及其相应值倒换角色。<br/>";
?>

<p><a href=".">返回</a></p>
