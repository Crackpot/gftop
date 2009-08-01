<?php
    if($_POST["username"]){
        echo "用户名：",$_POST["username"];
    }
    elseif($_GET["age"]){
        echo "年龄：",$_GET["age"];
    }
    elseif($_REQUEST["bloodtype"]){
        echo "血型：",$_REQUEST["bloodtype"];
    }
    else{
        echo "您未提交任何信息！";
    }
?>
