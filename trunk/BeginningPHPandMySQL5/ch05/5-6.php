<h1>定位数组元素</h1>

<h2>1.in_array()</h2>
<?php
    $grades = array(100,94.7,67,89,100,"Crackpot");
    echo "数组grades为："."<br/>";
    print_r($grades);
    echo "<br/>";
    if(in_array("100",$grades)) echo "Sally studied for the test!"."<br/>";
    if(in_array("100",$grades,1)) echo "Joe studied for the test!"."<br/>";//第三个boolean型参数强制考虑搜索类型。此句要求数据类型必须匹配。
    if(in_array("100",$grades,0)) echo "Joe studied for the test!"."<br/>";//第三个boolean型参数强制考虑搜索类型
    if(in_array("Crackpot",$grades,1)) echo "发现数组元素Crackpot!"."<br/>";//第三个boolean型参数强制考虑搜索类型。此句要求数据类型必须匹配。
?>

<h2>2.array_keys()</h2>
<?php
    $states["Delaware"] = "December 7, 1787";
    $states["Pennsylvania"] = "December 12, 1787";
    $states["New Jersey"] = "December 18, 1787";
    echo "数组states为："."<br/>";
    print_r($states);

    echo "<br/>";
    echo "数组states提取所得的键为："."<br/>";
    $keys = array_keys($states);
    print_r($keys);
?>

<h2>3.array_key_exists()</h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states["Delaware"] = "December 7, 1787";
    $states["Pennsylvania"] = "December 12, 1787";
    $states["Ohio"] = "March 1, 1787";
    echo "数组states为："."<br/>";
    print_r($states);

    echo "<br/>";
    if(array_key_exists("Delaware",$states)) echo "Delaware joined the Union on $states[Delaware]"."<br/>";
    if(array_key_exists("Pennsylvania",$states)) echo "Pennsylvania joined the Union on $states[Pennsylvania]"."<br/>";
    if(array_key_exists("Ohio",$states)) echo "Ohio joined the Union on $states[Ohio]"."<br/>";
    if(!array_key_exists("New York",$states)) echo "There is no information about New York!"."<br/>";
?>

<h2>4.array_values()</h2>
<?php
    $population = array(
        "Ohio" => "11,421,267",
        "Iowa" => "2,936,760",
        );
    echo "数组population为："."<br/>";
    print_r($population);

    echo "<br/>";
    echo "数组population的键为："."<br/>";
    $popkeys = array_keys($population);
    print_r($popkeys);

    echo "<br/>";
    echo "数组population的值为："."<br/>";
    $popvalues = array_values($population);
    print_r($popvalues);
?>

<h2>5.array_search()</h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states["Ohio"] = "March 1";
    $states["Delaware"] = "December 1";
    $states["Pennsylvania"] = "December 12";
    $founded = array_search("December 12",$states);
    echo "数组states为："."<br/>";
    print_r($states);

    echo "<br/>";
    if($founded) echo "The state $founded was founded on $states[$founded]";
?>
