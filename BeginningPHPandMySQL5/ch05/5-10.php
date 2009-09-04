<h1>合并、拆分、接合和分解数组</h1>

<h2>1.array_combine() 合并数组，两数组大小必须相同</h2>
<?php
    echo "两个数组分别对应key和value，其大小必须相同"."<br/>";
    echo "数组abbreviations为："."<br/>";
    $abbreviations = array("AL","AK","AZ","AR");
    print_r($abbreviations);

    echo "<br/>";
    echo "数组states为："."<br/>";
    $states = array("Alabama","Alaska","Arizona","Arkansas");
    print_r($states);

    echo "<br/>";
    echo "以上数组的合并数组stateMap为："."<br/>";
    $stateMap = array_combine($abbreviations, $states);
    print_r($stateMap);
?>
<h2>2.array_merge() 数组追加，返回联合数组</h2>
<?php
    echo "数组face为："."<br/>";
    $face = array("J","Q","K","A",);
    print_r($face);

    echo "<br/>";
    echo "数组numbered为："."<br/>";
    $numbered = array("2","3","4","5","6","7","8","9","10",);
    print_r($numbered);

    echo "<br/>";
    echo "数组face和numbered的组合数组cards为："."<br/>";
    $cards = array_merge($face,$numbered);
    print_r($cards);

    echo "<br/>";
    echo "用shuffle()函数对数组cards洗牌："."<br/>";
    shuffle($cards);
    print_r($cards);
?>

<h2>3.array_merge_recursive() </h2>
<?php
    echo "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array_merge_recursive()和array_merge()功能相同，可以将两个或多个数组合并在一起，形成一个联合的数组。其区别在于，当某个输入数组中的某个键已经存在于结果数组中时会以怎样的处理方式。array_merge会覆盖前面存在的键/值对，替换为当前输入数组的键/值对，而array_merge_recursive()将把两个值合并在一起，形成一个新的数组，并以现有的键作为数组名。"."<br/>";

    echo "数组class1为："."<br/>";
    $class1 = array("John" => 100, "James" => 85);
    print_r($class1);

    echo "<br/>";
    echo "数组class2为："."<br/>";
    $class2 = array("Micky" => 78, "John" => 45);
    print_r($class1);

    echo "<br/>";
    echo "以上数组的联合数组classScores为："."<br/>";
    $classScores = array_merge_recursive($class1, $class2);
    print_r($classScores);
?>

<h2>4.array_slice()</h2>
<?php
    unset($states);//注销上个部分创建的数组states
    echo "数组states为："."<br/>";
    $states = array("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut");
    print_r($states);

    echo "<br/>";
    echo "以上数组的分片数组subset为："."<br/>";
    $subset = array_slice($states, 4);
    print_r($subset);
?>

<h2>5.array_splice()</h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states = array("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut");
    $subset = array_splice($states, 4);
    print_r($states);
    echo "<br/>";
    print_r($subset);
?>

<h2>6.array_intersect()</h2>
<?php?>

<h2>7.array_intersect_assoc()</h2>
<?php?>

<h2>8.array_diff()</h2>
<?php?>

<h2>8.array_diff_assoc()</h2>
<?php?>
