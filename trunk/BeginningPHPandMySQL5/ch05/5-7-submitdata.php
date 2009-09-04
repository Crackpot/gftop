<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<?php
    function sanitize_data(&$value, $key){
        $value = strip_tags($value);//清除空格
        echo "第 $key 个值是： $value"."<br/>";
    }

    array_walk($_POST['keyword'],"sanitize_data");
?>
