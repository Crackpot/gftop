<?php
    if ($_POST['name']&&$_POST['age']){
    //如果没有信息提交就显示其他内容
?>
你好，<?php
    echo $_POST['name'];
?>。
<br/>
您<?php
    echo $_POST['age'];
?>岁了。
<?php
    }else{
        echo '您未提交任何信息！';
    }
?>