<h3>打印整个超级全局变量列表</h3>
<?php
    foreach($_SERVER as $var => $value){
        echo "$var => $value <br/>";
    }
    echo "<br/>";
?>

<h4>1、$_SERVER</h4>
<?php
    echo "引导用户到达当前位置的页面的URL："."<br/>";
    echo "\$_SERVER['HTTP_REFER'] => ".$_SERVER['HTTP_REFER']."<br/>";
    echo "服务端IP地址："."<br/>";
    echo "\$_SERVER['SERVER_ADDR'] => ".$_SERVER['SERVER_ADDR']."<br/>";
    echo "客户端IP地址："."<br/>";
    echo "\$_SERVER['REMOTE_ADDR'] => ".$_SERVER['REMOTE_ADDR']."<br/>";
    echo "URL的路径部分："."<br/>";
    echo "\$_SERVER['REQUEST_URI'] => ".$_SERVER['REQUEST_URI']."<br/>";
    echo "客户的用户代理："."<br/>";
    echo "\$_SERVER['HTTP_USER_AGENT'] => ".$_SERVER['HTTP_USER_AGENT']."<br/>";
?>

<h4>2、$_GET</h4>
<?php
    $_GET['username'] = "crackpot";
    echo "\$_GET['username'] = ".$_GET['username']."<br/>";
    $_GET['age'] = 23;
    echo "\$_GET['age'] = ".$_GET['age']."<br/>";
?>

<h4>3、$_POST</h4>

<?php
    if($_POST['username']&&$_POST['password']){
        echo "登录成功！<br/>";
        echo "用户名 (\$_POST['username']) => ".$_POST['username']."<br/>";
        echo "密码 (\$_POST['password']) => ".$_POST['password']."<br/>";
        echo "登录按钮 (\$_POST['subscribe']) => ".$_POST['subscribe']."<br/>";
    }
    else{
        echo "未登录！";
?>
    <form action="3-6-3.php" method="post">
        <p>
            用户名:<br/>
            <input type="text" name="username" size="20" maxlenght="50" value="">
        </p>
        <p>
            密码:<br/>
            <input type="password" name="password" size="20" maxlenght="15" value="">
        </p>
        <p>
            <input type="submit" name="subscribe" value="提交">
        </p>
    </form>
<?php
    }
?>

<h4>4、$_COOKIE</h4>
<h6>待完善 详见18章</h6>
<?php?>

<h4>5、$_FILES</h4>
<h6>待完善 详见15章</h6>
<?php?>

<h4>6、$_ENV</h4>
<?php
    echo "\$_ENV['HOSTNAME'] => ".$_ENV['HOSTNAME']."<br/>";
    echo "\$_ENV['HOSTTYPE'] => ".$_ENV['HOSTTYPE']."<br/>";
    echo "\$_ENV['SHELL'] => ".$_ENV['SHELL']."<br/>";
?>

<h4>7、$_REQUEST</h4>
<h6>待完善 详见21章</h6>
<?php?>

<h4>8、$_SESSION</h4>
<h6>待完善 详见18章</h6>
<?php?>

<h4>9、$GLOBALS</h4>
<p>超级全局变量的超集</p>
<?php
    echo "<pre>";
    print_r($GLOBALS);
    echo "</pre>";
?>

<a href="./">返回</a>
