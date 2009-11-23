<?php
require_once('include/logined.php');
if (is_logined()) {// 已登录
  echo '已登录';
}// 已登录
else {// 未登录
  echo '<TABLE ALIGN="center" WIDTH="400">
    <TBODY ALIGN="center">
      <TR>
        <TD><A HREF="index.php">首页</A></TD>
        <TD><A HREF="login.php">登录</A></TD>
        <TD><A HREF="signup.php">注册</A></TD>
      </TR>
      </TBODY>
    </TABLE>';
}// 未登录
?>
