<?php
    if (strpos($_SERVER['HTTP_USER_AGENT'],'MSIE')!==false){
?>
<h3>测试您的浏览器类型</h3>
<p>正在使用IE</p>
<?php
    }
    elseif(strpos($_SERVER['HTTP_USER_AGENT'],'Firefox')==true){
?>
<h3>测试您的浏览器类型</h3>
<center>
    <b>您使用的浏览器是火狐</b>
</center>
<?php
    }
    elseif(strpos($_SERVER['HTTP_USER_AGENT'],'Presto')==true){
?>
<h3>测试您的浏览器类型</h3>
<center>
    <b>您使用的浏览器是Opera</b>
</center>
<?php
    }
?>
<!--
    strpos() 是 PHP 的一个内置函数，其功能是在一个字符串中搜索另外一个字符串。
    echo $_SERVER[HTTP_USER_AGENT];打印出来的内容如下：
    Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.0.11) Gecko/2009060200 SUSE/3.0.11-0.1.1 Firefox/3.0.11
    Opera/9.64 (X11; Linux i686; U; Edition IBIS; zh-cn) Presto/2.1.1
    浏览器的类型在最后一个斜杠前
-->