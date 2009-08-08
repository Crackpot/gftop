<h3>1.数组</h3>
<?php
    echo "<h5>a.数字索引</h4>";
    $state[0] = "Alabama";
    echo "state[0] = $state[0]"."<br/>";
    $state[1] = "Alaska";
    echo "state[1] = $state[1]"."<br/>";
    $state[2] = "Arizona";
    echo "state[2] = $state[2]"."<br/>";

    echo "<h5>b.关联索引</h4>";
    $state["Alabama"] = "Montgomery";
    echo "state[\"Alabama\"] = ".$state["Alabama"]."<br/>";
    $state["Alaska"] = "Juneau";
    echo "state[\"Alaska\"] = ".$state["Alaska"]."<br/>";
    $state["Arizona"] = "Phoenix";
    echo "state[\"Arizona\"] = ".$state["Arizona"]."<br/>";
?>
<h3>2.对象</h3>
<?php
    echo "创建类和对象"."<br/>";
    class appliance{
        function setPower($status){
            $this->power = $status;
        }
    }
    $blender = new appliance;
    echo $blender;
?>
