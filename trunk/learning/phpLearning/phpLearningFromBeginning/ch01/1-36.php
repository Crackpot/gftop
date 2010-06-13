<meta http-equiv="Content-Type" content="text/html; charset=utf8" />
<?php
    if($_POST["name"] && $_POST["hometown"])//两个信息都不为空
    {
        echo "大家好，我是", $_POST["name"] , "<br/>";   
        //echo $_POST["username"] + "<br/>";   
        echo "我来自",$_POST["hometown"], "<br>";
    }
    else{
        echo "您未提交任何数据！请从提交表单重新提交信息";   
    }
?>
