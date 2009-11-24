<?php
// 页眉
$page_title = '注册';
require_once('include/header.php');

require_once('include/config.php');

// 连接数据库
$dbc = @mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) or die('数据库连接错误，请检查参数设置！');

if (isset($_POST['submit'])) {// 提交表单
  $username = mysqli_real_escape_string($dbc, trim($_POST['username']));
  $password1 = mysqli_real_escape_string($dbc, trim($_POST['password1']));
  $password2 = mysqli_real_escape_string($dbc, trim($_POST['password2']));
}// 提交表单
?>

<DIV ALIGN="center" WIDTH="400">
  <FORM METHOD="post" ACTION="signup.php">
    <FIELDSET STYLE="width: 300px;">
      <LEGEND>注册信息</LEGEND>
      <TABLE>
        <TR>
          <TD>
            <!-- 用户名 -->
            <LABEL FOR="username">用户名:</LABEL>
          </TD>
          <TD>
            <INPUT TYPE="TEXT" NAME="username" VALUE="" SIZE="20"><BR>
          </TD>
        </TR>
        <TR>
          <!-- 密码 -->
          <TD>
            <LABEL FOR="password1">密码:</LABEL>
          </TD>
          <TD>
            <INPUT TYPE="PASSWORD" NAME="password1" VALUE="" SIZE="20"><BR>
          </TD>
        </TR>
        <TR>
          <TD>
            <LABEL FOR="password2">确认密码:</LABEL>
          </TD>
          <TD>
            <INPUT TYPE="PASSWORD" NAME="password2" VALUE="" SIZE="20"><BR>
          </TD>
        </TR>
        <TR>
          <!-- 邮箱 -->
          <TD>
            <LABEL FOR="email">邮箱:</LABEL>
          </TD>
          <TD>
            <INPUT TYPE="TEXT" NAME="email" VALUE="" SIZE="20">
          </TD>
        </TR>
        <!-- 用户组 -->
<?php
$query_group = "SELECT * FROM yj_administrator_group";
$data_group = mysqli_query($dbc, $query_group) or die ('检索用户组失败');
if (mysqli_num_rows($data_group) >0) {// 检索到记录
echo '<TR>
  <TD><LABEL FOR="group_id">用户组:</LABEL></TD>';
  $groups = array();// 用一个数组盛放所有检索到的记录
  while ($row = mysqli_fetch_array($data_group)) {// 依次遍历各条记录
    /*
     * 在此将$row中的数据全部转向另外一个数组时，将来读取数据时候用新数组的名称
     * */
    array_push($groups, $row);// 将检索到的行结果添加到数组groups的最后
    //echo '检索到'.$row['group_id']. $row['group_name'];
  }// 依次遍历各条记录

  /*
  echo '<PRE>';
  print_r($groups);
  echo '</PRE>';
   */

  echo '<TD><SELECT NAME="group_id">';
  echo '<OPTION VALUE="-1">请选择</OPTION>';
  foreach ($groups as $group) {
    //print_r($group);
    $group_id = $group['group_id'];
    $group_name = $group['group_name'];
    //echo '检索到'.$group_id. $group_name;
    echo '<OPTION VALUE="' . $group_id . '">'. $group_name . '</OPTION>';
  }
  echo '</SELECT></TD></TR>';
}// 检索到记录

#mysqli_close($dbc);
?>
        </TR>
        <!-- 店面 -->
<?php
$query_storefront = "SELECT * FROM yj_storefront";
$data_storefront = mysqli_query($dbc, $query_storefront) or die('检索店面信息失败');
if ($row = mysqli_num_rows($data_storefront) > 0) {// 检索到记录
echo '<TR>
  <TD><LABEL FOR="storefront">店面:</LABEL></TD>';
  $storefronts = array();
  while($row = mysqli_fetch_array($data_storefront)) {// 依次遍历各条记录
    array_push($storefronts, $row);
  }// 依次遍历各条记录
  echo '<TD><SELECT NAME="storefront_id">';
  echo '<OPTION VALUE="-1">请选择</OPTION>';
  foreach($storefronts as $storefront) {
    $storefront_id = $storefront['storefront_id'];
    $storefront_name = $storefront['storefront_name'];
    echo '<OPTION VALUE="' . $storefront_id . '">' . $storefront_name . '</OPTION>';
  }
  echo '</SELECT></TD></TR>';
}// 检索到记录
?>
        <TR>
          <TD COLSPAN="2" ALIGN="center">
            <INPUT TYPE="SUBMIT" NAME="submit" VALUE="提交">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <INPUT TYPE="RESET" VALUE="重置">
          </TD>
        </TR>
      </TABLE>
    </FIELDSET>
  </FORM>
</DIV>
<?php
require_once('include/footer.php');
?>
