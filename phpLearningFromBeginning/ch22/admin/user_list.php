<?php
if(isset($_GET['o']))
    $op = $_GET['o'];
else
    $op = '';
if($op=='r')                 //���û�ID����
{
    $tmp_sql = "order by user_id desc";
}
elseif($op == 'l')           //����¼ʱ������
{
    $tmp_sql = "order by login_time desc";
}
else
    $tmp_sql = "";

$info = "<a href=\"user_list.php\" style=\"font-size: 13px;\">�г�����</a> ";
$info .="<a href=\"?o=r\" style=\"font-size: 13px;\">������ע������</a>    ";
$info .= "<a href=\"?o=l\" style=\"font-size: 13px;\">�������¼����</a><br/><br/>";
$info .= "<table border=1 style=\"font-size: 13px;\"><tr bgcolor=\"#abcdef\" align=\"center\">";
$info .= "<td><b>�û�ID</b></td><td><b>�û���</b></td><td><b>Email</b></td><td><b>ע��ʱ��</b></td>";
$info .= "<td><b>ע��IP</b></td><td><b>��¼ʱ��</b></td><td><b>��¼IP</b></td><td><b>����</b></td></tr>";

mysql_connect("localhost","root","admin");
mysql_select_db("mybbs") or die("Can't select database");

if(!empty($_GET['del']))     //ɾ���û��Ĳ���
{
    $user_id = $_GET['del'];
    $sql = "delete from users where user_id=".$user_id;
    mysql_query($sql) or die ('ERROR: '.mysql_error());
}

$sql = "select user_id,user_name,email,reg_ip,reg_time,login_ip,login_time from users ".$tmp_sql;
$result = mysql_query($sql) or die ('ERROR: '.mysql_error());
if(mysql_num_rows($result))
{
    while($row = mysql_fetch_array($result))
    {
        if(empty($row['email']))
            $email = "δ��д";
        else
            $email = $row['email'];
        $info .= "<tr><td>".$row['user_id']."</td><td>".$row['user_name']."</td><td>".$email;
        $info .= "</td><td>".$row['reg_time']."</td><td>".$row['reg_ip'];
        $info .= "</td><td>".$row['login_time']."</td><td>";
        $info .= $row['login_ip']."</td><td><a href=\"?del=".$row['user_id']."\">ɾ��</a></td><tr>";
    }
    $info .= "</table>";
}
else
{
    $info = "����ע���û���Ϣ";
}
echo $info;
?>