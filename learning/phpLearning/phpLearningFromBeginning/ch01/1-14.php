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
    elseif($_POST["username1"]&&$_POST["age1"]&&$_POST["bloodtype1"]){
        echo "用户名：",$_POST["username1"]."<br/>";
        echo "年龄：",$_POST["age1"]."<br/>";
        echo "血型：",$_POST["bloodtype1"]."<br/>";
    }
    else{
        echo "您未提交任何信息！";
    }
?>
