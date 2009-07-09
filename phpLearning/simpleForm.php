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
<!--
    该脚本进行的工作应该已经很明显了，这儿并没有其它更复杂的内容。PHP 将自动设置 $_POST['name'] 和 $_POST['age'] 变量。在这之前我们使用了自动全局变量 $_SERVER，现在我们引入了自动全局变量 $_POST，它包含了所有的 POST 数据。请注意我们的表单提交数据的方法（method）。如果使用了 GET 方法，那么表单中的信息将被储存到自动全局变量 $_GET  中。如果并不关心请求数据的来源，也可以用自动全局变量 $_REQUEST，它包含了所有 GET、POST、COOKIE 和 FILE 的数据。请参阅 import_request_variables() 函数。 
-->