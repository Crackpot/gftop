<h1>确定数组大小和唯一性</h1>

<h2>1.count() sizeof()</h2>
<?php
    $garden = array("cabbage","peppers","turnips","carrots",);
    echo "数组garden为："."<br/>";
    print_r($garden);
    echo "<br/>";
    echo "其元素的个数为：".count($garden)."<br/>";

    echo "<br/>";
    $locations = array("Italiy","Amsterdam",array("Boston","Des Moines"),"Miami",);
    echo "数组locations为："."<br/>";
    print_r($locations);
    echo "<br/>";
    echo "count()函数不加可选参数时，其元素的个数为：".count($locations)."<br/>";
    echo "sizeof()函数不加可选参数时，其元素的个数为：".sizeof($locations)."<br/>";
    echo "count()函数参数为1时，其元素的个数为：".count($locations,1)."<br/>";
    echo "sizeof()函数参数为1时，其元素的个数为：".sizeof($locations,1)."<br/>";
?>

<h2>2.array_count_values()</h2>
<?php
    $states = array("Ohio","Iowa","Arizona","Iowa","Ohio",);
    echo "数组states为："."<br/>";
    print_r($states);
    echo "<br/>";
    $stateFrequency = array_count_values($states);
    echo "数组stateFrequency为："."<br/>";
    print_r($stateFrequency);
    echo "<br/>";
    echo "其记录了数组states中元素分别出现的次数。"."<br/>";
?>

<h2>3.array_unique()</h2>
<?php
    $states = array("Ohio","Iowa","Arizona","Iowa","Ohio",);
    echo "数组states为："."<br/>";
    print_r($states);
    echo "<br/>";

    $uniqueStates = array_unique($states);
    echo "经过array_unique处理所得的数组uniqueStates为："."<br/>";
    print_r($uniqueStates);
?>
