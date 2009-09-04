<h1>创建数组</h1>

<?php
    echo "<b>为数组索引映射新值：</b>"."<br/>";
    $states[0] = "Delaware";
    echo "\$states[0] = ".$states[0]."<br/>";
    $states[1] = "Pennsylvania";
    echo "\$states[1] = ".$states[1]."<br/>";
    $states[2] = "New Jersey";
    echo "\$states[2] = ".$states[2]."<br/>";
    $states[49] = "Hawaii";
    echo "\$states[49] = ".$states[49]."<br/>";
    echo "<pre>";
    print_r($states);
    echo "</pre>";
?>
<br/>
<?php
    echo "<b>索引值是数值索引且是递增的，可以在创建时省略索引值：</b>"."<br/>";
    unset($states);//注销上个部分创建的数组states
    $states[] = "Delaware";
    $states[] = "Pennsylvania";
    $states[] = "New Jersey";
    $states[] = "Hawaii";
    echo "\$states[0] = ".$states[0]."<br/>";
    echo "\$states[1] = ".$states[1]."<br/>";
    echo "\$states[2] = ".$states[2]."<br/>";
    echo "\$states[3] = ".$states[3]."<br/>";
    echo "\$states[4] = ".$states[4]."<br/>";
    echo "<pre>";
    print_r($states);
    echo "</pre>";
?>
<br/>
<?php
    echo "<b>将美国州名映射到其他加入联盟的日期：</b>"."<br/>";
    unset($states);//注销上个部分创建的数组states
    $states["Delaware"] = "December 7, 1787";
    $states["Pennsylvania"] = "December 12, 1787";
    $states["New Jersey"] = "December 18, 1787";
    $states["Hawaii"] = "December 21, 1787";
    echo "<pre>";
    print_r($states);
    echo "</pre>";
?>
<h2>1.array()</h2>
<?php
    echo "array()接受0个或者多个元素作为输入，返回一个包含这些输入元素的数组"."<br/>";
    $language = array(
        "English",
        "Gaelic",
        "Spanish",
        );
    print_r($language);
    echo "<br/>";

    unset($language);//注销上个部分创建的数组language
    echo "array()指定下标创建数组"."<br/>";
    $language[0] = "English"; 
    $language[1] = "Gaelic";
    $language[2] = "Spanish";
    print_r($language);
    echo "<br/>";

    echo "array()创建一个关联数组"."<br/>";
    unset($language);//注销上个部分创建的数组language
    $language = array(
        "Spain" => "Spanish",
        "Ireland" => "Gaelic",
        "United States" => "English",
        );
    print_r($language);
?>
<h2>2.list()</h2>
<?php
    $user_file=fopen("5-3.txt","r");//创建文件对象
    while($line = fgets($user_file,4096)){//读取的此行内容有效
        list($name,$occupation,$color,) = explode("|",$line);//将读取的没行内容以"|"分开，分别赋值给列表中的三个元素
        print "Name: $name <br/>";
        print "Occupation: $occupation <br/>";
        print "Favorite Color: $color <br/>";
        echo "<br/>";
    }
?>
<h2>3.range()</h2>
<?php
    echo "利用range()快速创建0到6的数组："."<br/>";
    $die = range(0,6);//相当于$die = array(0,1,2,3,4,5,6);
    print_r($die);

    echo "<br/>";
    echo "利用range()快速创建0到20，步长为2的数组："."<br/>";
    $even = range(0,20,2);
    print_r($even);

    echo "<br/>";
    echo "利用range()快速创建A到Z，步长为2的数组："."<br/>";
    $letters = range(A,Z,2);
    print_r($letters);
?>
