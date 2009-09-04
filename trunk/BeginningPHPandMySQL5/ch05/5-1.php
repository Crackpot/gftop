<h1>什么是数组</h1>

<?php
    $ms_office = array(
        "word",
        "excel",
        "outlook",
        "access",
    );

    echo "<pre>";
    echo "值数组ms_office如下："."<br/>";
    print_r($ms_office);
    echo "下标为2的元素为：".$ms_office[2];
    echo "</pre>";
    echo "<br/>";
?>
<?php
    $states = array(
        "OH" => "Ohio",
        "PA" => "Pennsylvania",
        "NY" => "New York",
    );

    echo "<pre>";
    echo "关联数组states如下："."<br/>";
    print_r($states);
    echo "关联为'PA'的元素为：".$states["PA"];
    echo "</pre>";
    echo "<br/>";
?>

<?php
    $states = array(
        "Ohio" => array("population" => "11,353,140","captial" => "Columbus",),
        "Nebraska" => array("population" => "1,711,263","captial" => "Omaha",),
    );
    echo "<pre>";
    echo "二级关联数组states如下："."<br/>";
    print_r($states);
    echo "Nebraska的首都：".$states["Nebraska"]["captial"]."<br/>";
    echo "Nebraska的人口：".$states["Nebraska"]["population"]."<br/>";
    echo "</pre>";
    echo "<br/>";
?>
