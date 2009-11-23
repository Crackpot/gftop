<?php
require_once('include/config.php');
require_once('include/logined.php');

session_start();

// 清除错误信息
$error_msg = "";

if (!is_logined()) {// 未登录
  if (isset($_POST['submit'])) {// 已提交表单
  }// 已提交表单
}// 未登录

// 页眉
$page_title = '登录';
require_once('include/header.php');

if (empty($_SESSION['user_id']) && empty($_SESSION['user_uuid'])) {// 值为空
  echo '<P CLASS="error">' . $error_msg . '</P>';
?>
<FORM METHOD="post" ACTION="login.php">
  <DIV WIDTH="100%" ALIGN="center">
    <FIELDSET STYLE="width: 300px;">
      <LEGEND>登录</LEGEND>
      <TABLE>
        <TR>
          <!-- 管理员名称 -->
          <TD>
            <LABEL FOR="user_name">管理员名称:</LABEL>
          </TD>
          <TD>
            <INPUT TYPE="TEXT" NAME="user_name" VALUE="<?php if (!empty($user_name)) echo $user_name; ?>" SIZE="20">
          </TD>
        </TR>
        <TR>
          <TD>
            <LABEL FOR="password">密码:</LABEL>
          </TD>
          <TD>
            <INPUT TYPE="PASSWORD" NAME="password" VALUE="" SIZE="20">
          </TD>
        </TR>
        <TR>
          <TD COLSPAN="2" ALIGN="center">
            <INPUT TYPE="SUBMIT" NAME="submit" VALUE="提交">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <INPUT TYPE="RESET" VALUE="重置">
          </TD>
        </TR>
      </TABLE>
    </FIELDSET>
  </DIV>
</FORM>
<?php
}// 值为空
// 页脚
require_once('include/footer.php');

?>
