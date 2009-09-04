<h1>数组排序</h1>

<h2>1.sort() 正向排序</h2>
<?php
    $grade = array(42,57,98,100,100,43,78,12,);
    echo "数组grade为："."<br/>";
    print_r($grade);
    echo "<br/>";

    echo "用sort()对数组grade排序后为："."<br/>";
    sort($grade);
    print_r($grade);

    echo "<br/>";
    echo "<br/>";
    $garden = array("cabbage","peppers","turnips","carrots",);
    echo "数组garden为："."<br/>";
    print_r($garden);

    echo "<br/>";
    echo "用sort()对数组garden排序后为："."<br/>";
    sort($garden);
    print_r($garden);

    echo "<br/>";
    echo "<br/>";
    $locations = array("Italiy","Amsterdam",array("Boston","Des Moines"),"Miami",);
    echo "数组locations为："."<br/>";
    print_r($locations);

    echo "<br/>";
    echo "用sort()对数组locations排序后为："."<br/>";
    sort($locations);
    print_r($locations);
?>

<h2>2.natsort() 字符串数字组合排序</h2>
<?php
    $pictures = array("picture1.jpg","picture20.jpg","picture2.jpg","picture10.jpg",);
    echo "数组pictures为："."<br/>";
    print_r($pictures);

    echo "<br/>";
    echo "用sort()对数组pictures排序后为："."<br/>";
    sort($pictures);
    print_r($pictures);

    echo "<br/>";
    echo "用nasort()对数组pictures排序后为："."<br/>";
    natsort($pictures);
    print_r($pictures);
?>

<h2>3.natcasesort() 大小写不规则排序</h2>
<?php
    unset($pictures);//注销上个部分创建的数组pictures
    $pictures = array("PICTURE10.jpg","Picture1.jpg","picture20.jpg","picture2.jpg",);
    echo "数组pictures为："."<br/>";
    print_r($pictures);

    echo "<br/>";
    echo "用sort()对数组pictures排序后为："."<br/>";
    sort($pictures);
    print_r($pictures);

    echo "<br/>";
    echo "用natsort()对数组pictures排序后为："."<br/>";
    natsort($pictures);
    print_r($pictures);

    echo "<br/>";
    echo "用natcasesort()对数组pictures排序后为："."<br/>";
    natcasesort($pictures);
    print_r($pictures);
?>

<h2>4.rsort() 反向排序</h2>
<?php
    $states = array("Ohio","Florida","Massachusetts","Montana",);
    echo "数组states为："."<br/>";
    print_r($states);

    echo "<br/>";
    echo "用sort()对数组states排序后为："."<br/>";
    sort($states);
    print_r($states);

    echo "<br/>";
    echo "用rsort()对数组states排序后为："."<br/>";
    rsort($states);
    print_r($states);
?>

<h2>5.asort() 升序排序，同时保持键值的关联</h2>
<?php
    echo "用asort()与sort()相同，以升序排序目标数组，只是它将保持键/值的关联。"."<br/>";
    unset($states);//注销上个部分创建的数组states
    $states[0] = "Delaware";
    $states[1] = "Pennsylvania";
    $states[2] = "New Jersey";

    echo "数组states为："."<br/>";
    print_r($states);

    echo "<br/>";
    echo "用asort()对数组states排序后为："."<br/>";
    asort($states);
    print_r($states);

    echo "<br/>";
    echo "用sort()对数组states排序后为："."<br/>";
    sort($states);
    print_r($states);
    echo "&nbsp;可见，用sort()对数组排序会丢掉键/值的关联，这样并不好。"."<br/>";
?>

<h2>6.array_multisort() 对多个数组排序</h2>
<?php
    $staff["givename"][0] = "Jason";
    $staff["givename"][1] = "Manny";
    $staff["givename"][2] = "Gary";
    $staff["givename"][3] = "James";

    $staff["surname"][0] = "Gilmore";
    $staff["surname"][1] = "Champy";
    $staff["surname"][2] = "Grisold";
    $staff["surname"][3] = "Gilmore";

    echo "数组staff为："."<br/>";
    print_r($staff);

    echo "<br/>";
    echo "数组staff[givename]为："."<br/>";
    print_r($staff["givename"]);

    echo "<br/>";
    echo "数组staff[surname]为："."<br/>";
    print_r($staff["surname"]);

    echo "<br/>";
    echo "用array_multisort对整个数组staff进行排序为："."<br/>";
    $res = array_multisort($staff["surname"],SORT_STRING,SORT_ASC,
                           $staff["givename"],SORT_STRING,SORT_ASC);

    print_r($staff);
?>

<h2>7.arsort() 逆序排序，同时保持键值的关联</h2>
<?php
    unset($states);//注销上个部分创建的数组states
    $states = array("Delaware","Pennsylvania","New Jersey",);
    echo "数组states为："."<br/>";
    print_r($states);

    echo "<br/>";
    echo "用asort()对数组states排序后为："."<br/>";
    arsort($states);
    print_r($states);
?>

<h2>8.ksort() 按键对数组顺序排序</h2>
<?php
    $captial = array(
        "Ohio" => "Columbus",
        "Iowa" => "Des Moines",
        "Arizona" => "Phoenix",
    );

    echo "数组captial为："."<br/>";
    print_r($captial);

    echo "<br/>";
    echo "用ksort()对数组captial排序后为："."<br/>";
    ksort($captial);
    print_r($captial);
?>

<h2>9.krsort() 按键对数组逆序排序</h2>
<?php
    echo "数组captial为："."<br/>";
    print_r($captial);

    echo "<br/>";
    echo "用krsort()对数组captial排序后为："."<br/>";
    krsort($captial);
    print_r($captial);
?>

<h2>10.usort() 用户自定义比较算法排序</h2>
<?php
    $dates = array(
        "10-10-2003",
        "2-17-2002",
        "2-16-2003",
        "1-01-2005",
        "10-10-2004",
        );
    echo "数组dates为："."<br/>";
    print_r($dates);

    echo "<br/>";
    echo "用sort()对数组dates排序后为："."<br/>";
    sort($dates);
    print_r($dates);

    echo "<br/>";
    echo "用natsort()对数组dates排序后为："."<br/>";
    natsort($dates);
    print_r($dates);

    function Datesort($a, $b){

        // 两个相等就什么都不做。
        if ($a == $b) return 0;

        // 对两个日期进行拆解
        list($amonth, $aday, $ayear) = explode('-',$a);
        list($bmonth, $bday, $byear) = explode('-',$b);

        // 在1位月份前加一个0，使得月份都为2位数
        $amonth = str_pad($amonth, 2, "0", STR_PAD_LEFT);
        $bmonth = str_pad($bmonth, 2, "0", STR_PAD_LEFT);

        // 在1位日期前加一个0，使得日期都为2位数
        $aday = str_pad($aday, 2, "0", STR_PAD_LEFT);
        $bday = str_pad($bday, 2, "0", STR_PAD_LEFT);

        // 重新组装年月日
        $a = $ayear . $amonth . $aday;
        $b = $byear . $bmonth . $bday;

        // 看看是否a大于b
        return ($a > $b) ? 1 : -1;// 升序排列
        #return ($a < $b) ? 1 : -1;// 降序排列
    }

    echo "<br/>";
    echo "用usort()对数组dates排序后为："."<br/>";
    usort($dates, "DateSort");
    print_r($dates);
?>
