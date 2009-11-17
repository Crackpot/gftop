<?php
require_once('connectvars.php');
require_once('startsession.php');


$dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) or die('数据库连接或配置错误');
mysqli_query($dbc, 'SET NAMES "UTF8"');

if (isset($_GET['action'])) {// url中封装动作
  switch($_GET['action']) {
  case 'register':// 注册
    if (!isset($_POST['submit'])){// 未提交
      echo '用户注册<BR>';
?>
      <FORM METHOD="post" ACTION="user.php?action=register">
        <TABLE>
          <TR>
            <TD>姓名:</TD><TD><INPUT TYPE="TEXT" NAME="name" VALUE="" SIZE="20"></TD>
          </TR>
          <TR>
            <TD>性别:</TD><TD><INPUT TYPE="RADIO" NAME="gender" VALUE="1" CHECKED="checked">男&nbsp;<INPUT TYPE="RADIO" NAME="gender" VALUE="2">女</TD>
          </TR>
          <TR>
            <TD>手机</TD><TD><INPUT TYPE="TEXT" NAME="mobile" VALUE="" SIZE="20"></TD>
          </TR>
          <TR>
            <TD>Email:</TD><TD><INPUT TYPE="TEXT" NAME="email" VALUE="" SIZE="20"></TD>
          </TR>
          <TR>
            <TD>身份证号码:</TD><TD><INPUT TYPE="TEXT" NAME="identification_number" VALUE="" SIZE="20"></TD>
          </TR>
          <TR>
            <TD COLSPAN="2">为保障您的权益，现在填写真实证件号码，入住无需再次登记，体验快捷预订轻松入住。</TD>
          </TR>
          <TR>
            <TD COLSPAN="2"><INPUT TYPE="SUBMIT" NAME="submit" VALUE="提交">&nbsp;<INPUT TYPE="RESET" VALUE="Reset"></TD>
          </TR>
        </TABLE>
      </FORM>
<?php
    }// 未提交
    else {// 已提交
      $name = mysqli_real_escape_string($dbc, trim($_POST['name']));
      $gender = mysqli_real_escape_string($dbc, trim($_POST['gender']));
      $mobile = mysqli_real_escape_string($dbc, trim($_POST['mobile']));
      $email = mysqli_real_escape_string($dbc, trim($_POST['email']));
      $identification_number = mysqli_real_escape_string($dbc, trim($_POST['identification_number']));
      if (!empty($name) && !empty($gender) && !empty($mobile) && !empty($email) && !empty($identification_number)) {// 非空项非空
        $query = "SELECT * FROM yjswjd_user WHERE identification_number = '$identification_number'";
        $data = mysqli_query($dbc, $query) or die('查询用户失败');
        if (mysqli_num_rows($data) == 0) {// 未重复
          function MakePass($length)
          {
            $possible = "0123456789!@#$%^&*()_+".
             "abcdefghijklmnopqrstuvwxyz".
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            $str = "";
            while(strlen($str) < $length)
            {
              $str .= substr($possible, (rand() % strlen($possible)), 1);
            }
            #echo $str;
            return($str);
          }
          if (!isset($RandomPassword)) {
            $RandomPassword = MakePass(10);
          }
          if (isset($_COOKIE['RandomPassword'])) {
            setcookie('RandomPassword', '', time() - 3600);
          }
          else {
            setcookie('RandomPassword', $RandomPassword ,time() + 3600 * 24 *30);
          }
          $birthdateStr = substr($identification_number, 6, 8);
          $query = "INSERT INTO yjswjd_user (            user_id, name, password, join_date, birthdate,gender, mobile, email, identification_number) VALUES ('0', '$name', SHA('$RandomPassword'), NOW(), '$birthdateStr','$gender', '$mobile', '$email', '$identification_number')";
          mysqli_query($dbc, $query) or die('插入数据失败');
        }// 未重复
        else {// 重复
        }// 重复
      }// 非空项非空
      echo '注册成功<BR>';
      $query = "SELECT user_id FROM yjswjd_user WHERE identification_number = '" . $identification_number . "'";
      $data = mysqli_query($dbc, $query);
      $row = mysqli_fetch_array($data);
      $subject = "注册成功";
      $title = $gender==1 ? '先生':'女士';
      $body = "尊敬的" . $name . $title . "， 您好！".
        "您已成功注册！
        您的用户编号为: " . $row['user_id'] . ", 初始密码为: " . $_COOKIE['RandomPassword'] . "。";
          mail($email, $subject, $body);
      echo "您的会员号是：&nbsp;" . $row['user_id'] . "&nbsp;,初始密码为:&nbsp;" . $_COOKIE['RandomPassword'] ."<BR>";
      setcookie('RandomPassword', $RandomPassword ,time() + 3600 * 24 *30);
      echo '<A HREF="user.php?action=login">登录</A><BR>';
    }// 已提交
    break;
  case 'login':// 登录
    if (!isset($_SESSION['user_id'])) {// 用户未登录
      echo '用户未登录<BR>';
      if (!isset($_POST['submit'])) {// 未提交
?>
        <FORM ACTION="user.php?action=login">
          <TABLE>
            <TR>
              <TD>用户名:</TD>
              <TD><INPUT NAME="username" ID="username" TABINDEX="1" SIZE="20" VALUE="卡号/手机号码/身份证" STYLE="border: 1px solid rgb(204, 204, 204); background: rgb(255, 255, 255) none repeat scroll 0% 0%; -moz-background-clip: border; -moz-background-origin: padding; -moz-background-inline-policy: continuous; color: rgb(153, 153, 153); font-SIZE: 12px;" ONFOCUS="javascript:if (this.value=='卡号/手机号码/身份证')this.value='';this.style.Color='#0';" onblur=" javascript:if (this.value=='') {this.style.Color='#999';this.value='卡号/手机号码/身份证';}" TYPE="text"></TD>
            </TR>
            <TR>
              <TD>密码:</TD>
              <TD><INPUT TYPE="PASSWORD" NAME="password" ID="password" STYLE="border:1px solid rgb(204, 204, 204); width:130px;" TABINDEX="2" VALUE="" SIZE="20"></TD>
            </TR>
            <TR>
              <TD COLSPAN="2" ALIGN="center">
                <INPUT TYPE="SUBMIT" NAME="submit" VALUE="登录">
                <INPUT TYPE="RESET" VALUE="Reset"><BR>
                <A HREF="user.php?action=resetPassword">忘记密码</A>
              </TD>
            </TR>
          </TABLE>
        </FORM>
<?php
      }// 未提交
      else {// 已提交
        /*
      header("Content-Type: text/html; charset=utf-8");
      ob_start();//打开缓冲区
      $cookietime=time()+3600;//设置Cookie有效时间
      $user_id=$_POST['user_id'];//接收传过来的用户名
      $upwd=md5($_POST['upwd']);//接收传过来的密码并md5()
      $sql="SELECT * FROM yjswjd_user WHERE user_id='$user_id' AND u_pwd='$upwd'";//查询数据库
      $rs=mysql_query($sql);
      $num=@mysql_num_rows($rs);//获取查询结果的条数
      if(!($num>0))//0就是木有匹配的记录
      {
        echo "<script>alert('用户名或密码错误，请重新输入。');location.href='index.php'</script>";//重新登录去～
      }else{
        setcookie('uname',$uname,$cookietime);//设置Cookie
        setcookie('upwd',$upwd,$cookietime);
        echo "<script>location.href='xxx.php'</script>";//跳转
      }
      */
      }// 已提交
    }// 用户未登录
    else {// 用户已登录
      echo '用户已登录<BR>';
    }// 用户已登录
    break;
  case 'logout':// 退出
    echo '用户退出<BR>';
    break;
  }
}// url中封装动作
?>
<A HREF="./">return</A>
