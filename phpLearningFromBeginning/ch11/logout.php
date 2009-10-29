<?php
session_start();
$info = '';

if(isset($_SESSION['user']))
{
    $_SESSION['user'] = '';
    $msg = '您已经成功退出，<a href="index.php">返回首页</a>';
}
else
{
    $msg = '您未曾登录或已经超时退出，<a href="index.php">返回首页</a>';
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>基于文本的简易BLOG</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>

<div id="container">
    <div id="header">
        <h1><a href=".">我的BLOG</a></h1>
    </div>
    <div id="title">
        ----i have dream....
    </div>
    <div id="left">
        <div id="blog_entry">
            <div id="blog_title">退出登录</div>
            <div id="blog_body">
            <?php echo $msg; ?>
            </div><!--blog_body-->
        </div><!--blog_entry-->
    </div>
    
    <div id="right">
        <div id="sidebar">
            <div id="menu_title">关于我</div>
            <div id="menu_body">我是个PHP爱好者</div>
        </div>
    </div>
    
    <div id="footer">
        copyright 2007
    </div>
</div>

<body>
</html>
